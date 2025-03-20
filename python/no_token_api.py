from dataclasses import dataclass
from typing import Dict

import api_client
from api_client import APIError
from logger import RouterLogger


@dataclass
class InitInfo:
    is_support_mesh: bool
    sec_acc: bool
    inited: bool
    connect = bool
    modules: str
    replacement_assistant: bool
    hardware: str
    language: str
    romversion: str
    country_code: str
    id: str
    routername: str
    routername: str
    display_name: str
    maccel: bool
    model: str
    disable_telnet: bool
    bound: bool
    router_id: str
    is_redmi: bool


@dataclass
class FacInfo:
    wl0_ssid: str
    wl1_ssid: str
    telnet: str
    ssh: str
    facmode: str
    block_4k: bool
    secboot: bool
    uart: bool


@dataclass
class SysInfo:
    hardware: int
    routerName: int
    romVersion: int
    romChannel: str


@dataclass
class LanguageInfo:
    list_lang: str
    list_name: str
    lang: str


class NoTokenAPI:
    def __init__(self, master, router_ip: str):
        self.master = master
        self.router_ip = router_ip
        self.client = api_client.APIClient(router_ip, "", "", "")

    def _validate_response(self, data: Dict, required_fields: list) -> None:
        if data.get('code') != 0:
            raise APIError(f"API返回错误: {data.get('msg', '未知错误')}")
        missing = [field for field in required_fields if field not in data]
        if missing:
            raise APIError(f"响应缺少必要字段: {', '.join(missing)}")

    def get_init_info(self) -> InitInfo:
        try:
            data = self.client.get_init_info()
            self._validate_response(data,
                                    ['isSupportMesh', 'secAcc', 'inited', 'connect', 'modules',
                                     'replacement_assistant', 'hardware', 'language', 'romversion',
                                     'countrycode', 'id', 'routername', 'displayName', 'maccel', 'model',
                                     'DisableTencent', 'bound', 'routerId', 'isRedmi'])
            RouterLogger.log_operation("NoTokenAPI", f"成功获取初始化信息:{data}")
            return InitInfo(
                is_support_mesh=bool(data.get('isSupportMesh', 0)),
                sec_acc=bool(data.get('secAcc', 0)),
                inited=bool(data.get('inited', 0)),
                modules=data['modules'],
                replacement_assistant=bool(data.get('replacement_assistant', 0)),
                hardware=data['hardware'],
                language=data['language'],
                romversion=data['romversion'],
                country_code=data['countrycode'],
                id=data['id'],
                routername=data['routername'],
                display_name=data['displayName'],
                maccel=bool(data.get('maccel', 0)),
                model=data['model'],
                disable_telnet=bool(data.get('DisableTencent', 0)),
                bound=bool(data.get('bound', 0)),
                router_id=data['routerId'],
                is_redmi=bool(data.get('isRedmi', 0))
            )
        except Exception as e:
            RouterLogger.log_error("获取初始化信息失败", e)
            raise

    def get_fac_info(self) -> FacInfo:
        try:
            data = self.client.get_fac_info()
            self._validate_response(data,
                                    ['mac', 'wl0_ssid', 'wl1_ssid', 'telnet', 'ssh', 'facmode', 'block_4k',
                                     'secboot', 'uart'])
            RouterLogger.log_operation("NoTokenAPI", f"成功获取FAC信息:{data}")
            return FacInfo(
                wl0_ssid=data['wl0_ssid'],
                wl1_ssid=data['wl1_ssid'],
                telnet=data['telnet'],
                ssh=data['ssh'],
                facmode=data['facmode'],
                block_4k=bool(data.get('block_4k', 0)),
                secboot=bool(data.get('secboot', 0)),
                uart=bool(data.get('uart', 0))
            )
        except Exception as e:
            RouterLogger.log_error("获取FAC信息失败", e)
            raise

    def get_sys_info(self) -> SysInfo:
        try:
            data = self.client.get_sys_info()
            self._validate_response(data, ['hardware', 'routerName', 'romVersion', 'romChannel'])
            RouterLogger.log_operation("NoTokenAPI", f"成功获取系统信息:{data}")
            return SysInfo(
                hardware=data['hardware'],
                routerName=data['routerName'],
                romVersion=data['romVersion'],
                romChannel=data['romChannel']
            )
        except Exception as e:
            RouterLogger.log_error("获取系统信息失败", e)
            raise

    def get_languages(self) -> LanguageInfo:
        try:
            data = self.client.get_languages()
            self._validate_response(data, ['list - lang', 'list - name', 'lang'])
            RouterLogger.log_operation("NoTokenAPI", f"成功获取语言列表:{data}")
            return LanguageInfo(
                list_lang=data['list - lang'],
                list_name=data['list - name'],
                lang=data['lang']
            )
        except Exception as e:
            RouterLogger.log_error("获取语言列表失败", e)
            raise
