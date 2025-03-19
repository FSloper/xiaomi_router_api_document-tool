import hashlib
import json
import time
from typing import Optional, Dict, Any

import requests

from logger import RouterLogger
from login_router import login_router

NO_TOKEN_ENDPOINTS = {
    'xqsystem/init_info',
    'xqsystem/fac_info',
    'xqsystem/farewell',
    'xqsystem/sys_info',
    'xqsystem/get_languages',
    'xqsystem/get_main_language'
}


class APIClient:
    def __init__(self, router_ip: str, token: str, password: str, key: str):
        self.router_ip = router_ip
        self.token = token
        self.admin_pwd = password
        self.encrypt_key = key
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})

    def _generate_signature(self, data: dict) -> str:
        """生成API请求签名"""
        sorted_params = '&'.join([f'{k}={v}' for k, v in sorted(data.items())])
        return hashlib.md5(f'{sorted_params}{self.encrypt_key}'.encode()).hexdigest()

    def _request(self, endpoint: str, method: str = 'GET', params: Optional[dict] = None) -> Dict[str, Any]:
        """统一请求方法"""
        base_path = 'api/' if endpoint in NO_TOKEN_ENDPOINTS else f';stok={self.token}/api/'
        url = f'http://{self.router_ip}/cgi-bin/luci/{base_path}{endpoint}'

        try:
            params = params or {}
            params.update({
                'client': 'web',
                'lang': 'zh_cn',
                '_': str(int(time.time() * 1000))
            })
            params['sign'] = self._generate_signature(params)

            response = self.session.request(method, url, data=json.dumps(params))
            response.raise_for_status()

            result = response.json()
            if result.get('code') != 0:
                raise APIError(result.get('msg', '未知错误'))

            return result
        except requests.exceptions.RequestException as e:
            RouterLogger.log_error(f"API请求失败: {endpoint}", e)
            raise APIError(f"请求失败: {str(e)}")
        except json.JSONDecodeError as e:
            RouterLogger.log_error("响应解析失败", e)
            raise APIError("响应解析失败")

    def get_router_info(self) -> Dict[str, Any]:
        """获取路由器基本信息"""
        try:
            result = self._request('misystem/status')
            RouterLogger.log_operation("API_CALL", "获取路由器基本信息成功")
            return result
        except Exception as e:
            RouterLogger.log_error("获取路由器基本信息失败", e)
            raise

    def get_network_status(self) -> Dict[str, Any]:
        """获取网络接口状态"""
        try:
            result = self._request('misystem/wan_info')
            RouterLogger.log_operation("API_CALL", "获取网络状态成功")
            return result
        except Exception as e:
            RouterLogger.log_error("获取网络状态失败", e)
            raise

    def get_connected_devices(self) -> Dict[str, Any]:
        """获取已连接设备列表"""
        try:
            result = self._request('misystem/devicelist')
            RouterLogger.log_operation("API_CALL", f"获取到{len(result.get('list', []))}台已连接设备")
            return result
        except Exception as e:
            RouterLogger.log_error("获取设备列表失败", e)
            raise

    def get_init_info(self) -> Dict[str, Any]:
        """获取路由器初始化信息"""
        return self._request('xqsystem/init_info')

    def reboot_router(self) -> dict:
        """执行路由器重启操作"""
        return self._request('xqsystem/reboot')

    def refresh_token(self) -> str:
        """自动刷新token并返回新token"""
        new_token = login_router(self.router_ip, self.admin_pwd, self.encrypt_key)
        if new_token and new_token != self.token:
            self.token = new_token
        if new_token is not None:
            return new_token
        return ""


class APIError(Exception):
    """自定义API异常"""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
