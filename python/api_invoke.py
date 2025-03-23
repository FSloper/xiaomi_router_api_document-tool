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
    hardware: str
    language: str
    romversion: str
    countrycode: str
    id: str
    routername: str
    routername: str
    display_name: str
    maccel: bool
    model: str
    bound: bool
    routerId: str
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


@dataclass
class WanStatus:
    downspeed: str
    maxdownloadspeed: str
    upspeed: str
    maxuploadspeed: str
    download: str


@dataclass
class SysStatus:
    dev: str
    usage: str
    total: str
    hz_ddr: str
    type: str
    temperature: str
    online: str
    all: str
    mac: str
    platform: str
    version: str
    channel: str
    sn: str
    displayName: str
    upTime: str
    core: str
    hz_cpu: str
    download: str
    downspeed: int
    maxdownloadspeed: int
    upload: int
    upspeed: int
    maxuploadspeed: int


@dataclass
class Information:
    lan_ip: str
    wanType: str
    wan_ip: str
    dnsAddrs: str
    dnsAddrs1: str


def _validate_response(data: Dict, required_fields: list) -> None:
    if data.get('code') != 0:
        raise APIError(f"API返回错误: {data.get('msg', '未知错误')}")
    # missing = [field for field in required_fields if field not in data]
    # if missing:
    #     raise APIError(f"响应缺少必要字段: {', '.join(missing)}")


class NoTokenAPI:
    def __init__(self, master, router_ip: str):
        self.master = master
        self.router_ip = router_ip
        self.client = api_client.APIClient(router_ip, "", "", "")

    def get_init_info(self) -> InitInfo:
        try:
            data = self.client.get_init_info()
            _validate_response(data,
                               ['isSupportMesh', 'secAcc', 'inited', 'connect', 'modules',
                                'hardware', 'language', 'romversion',
                                'countrycode', 'id', 'routername', 'displayName', 'maccel', 'model',
                                'bound', 'routerId', 'isRedmi'])
            RouterLogger.log_operation("NoTokenAPI", f"成功获取初始化信息:{data}")
            return InitInfo(
                is_support_mesh=bool(data.get('isSupportMesh', 0)),
                sec_acc=bool(data.get('secAcc', 0)),
                inited=bool(data.get('inited', 0)),
                modules=data['modules'],
                hardware=data['hardware'],
                language=data['language'],
                romversion=data['romversion'],
                countrycode=data['countrycode'],
                id=data['id'],
                routername=data['routername'],
                display_name=data['displayName'],
                maccel=bool(data.get('maccel', 0)),
                model=data['model'],
                bound=bool(data.get('bound', 0)),
                routerId=data['routerId'],
                is_redmi=bool(data.get('isRedmi', 0))
            )
        except Exception as e:
            RouterLogger.log_error("获取初始化信息失败", e)
            raise

    def get_fac_info(self) -> FacInfo:
        try:
            data = self.client.get_fac_info()
            _validate_response(data,
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
            _validate_response(data, ['hardware', 'routerName', 'romVersion', 'romChannel'])
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
            _validate_response(data, ['list - lang', 'list - name', 'lang'])
            RouterLogger.log_operation("NoTokenAPI", f"成功获取语言列表:{data}")
            return LanguageInfo(
                list_lang=data['list - lang'],
                list_name=data['list - name'],
                lang=data['lang']
            )
        except Exception as e:
            RouterLogger.log_error("获取语言列表失败", e)
            raise


class NeedTokenAPI:
    def __init__(self, master, router_ip: str, token: str):
        self.master = master
        self.router_ip = router_ip
        self.client = api_client.APIClient(router_ip, token, "", "")

    def get_lan_wan_status(self) -> WanStatus:
        try:
            data = self.client.get_lan_wan_status()
            _validate_response(data, ['downspeed', 'maxdownloadspeed', 'upspeed', 'maxuploadspeed', 'download'])
            RouterLogger.log_operation("NeedTokenAPI", f"成功获取LAN和WAN状态:{data}")
            return WanStatus(
                downspeed=(data['downspeed']),
                maxdownloadspeed=data['maxdownloadspeed'],
                upspeed=data['upspeed'],
                maxuploadspeed=data['maxuploadspeed'],
                download=data['download']
            )
        except Exception as e:
            RouterLogger.log_error("获取LAN和WAN状态失败", e)
            raise

    def get_sys_status(self) -> SysStatus:
        try:
            data = self.client.get_sys_status()
            _validate_response(data, ['dev', 'usage', 'total', 'hz_ddr', 'type', 'temperature',
                                      'online', 'all', 'mac', 'platform', 'version', 'channel', 'sn',
                                      'displayName', 'upTime', 'core', 'hz_cpu', 'download', 'downspeed',
                                      'maxdownloadspeed', 'upload', 'upspeed', 'maxuploadspeed'])
            RouterLogger.log_operation("NeedTokenAPI", f"成功获取系统状态:{data}")
            online = data['upTime']
            hours = int(float(online) // 3600)
            minutes = int((float(online) % 3600) // 60)
            sys_time = f"{hours}小时{minutes}分钟"
            return SysStatus(
                dev=data['dev'],
                usage=data['mem']['usage'],
                total=data['mem']['total'],
                hz_ddr=data['mem']['hz'],
                type=data['mem']['type'],
                temperature=data['temperature'],
                online=data['count']['online'],
                all=data['count']['all'],
                mac=data['hardware']['mac'],
                platform=data['hardware']['platform'],
                version=data['hardware']['version'],
                channel=data['hardware']['channel'],
                sn=data['hardware']['sn'],
                displayName=data['hardware']['displayName'],
                upTime=sys_time,
                core=data['cpu']['core'],
                hz_cpu=data['cpu']['hz'],
                download=data['wan']['download'],
                downspeed=data['wan']['downspeed'],
                maxdownloadspeed=data['wan']['maxdownloadspeed'],
                upload=data['wan']['upload'],
                upspeed=data['wan']['upspeed'],
                maxuploadspeed=data['wan']['maxuploadspeed']
            )
        except Exception as e:
            RouterLogger.log_error("获取系统状态失败", e)
            raise

    def get_information(self) -> Information:
        try:
            data = self.client.get_information()
            _validate_response(data, ['lan_ip', 'wanType', 'wan_ip', 'dnsAddrs', 'dnsAddrs1'])
            RouterLogger.log_operation("NeedTokenAPI", f"成功获取信息:{data}")
            return Information(
                lan_ip=data['lan']['ipv4'][0]['ip'],
                wanType=data['wan']['details']['wanType'],
                wan_ip=data['wan']['gateWay'],
                dnsAddrs=data['wan']['dnsAddrs'],
                dnsAddrs1=data['wan']['dnsAddrs1']
            )
        except Exception as e:
            RouterLogger.log_error("获取信息失败", e)
            raise

    def get_device_list(self):
        try:
            data = self.client.get_device_list()
            devices = []
            for dev in data.get('list', []):
                data = dev['statistics']
                print(data)
                devices.append({
                    'type': dev.get('type', '未知连接方式'),
                    'ip': dev.get('ip', '0.0.0.0'),
                    'mac': dev.get('mac', 'N/A'),
                    'name': dev.get('name', '未知设备'),
                    'downspeed': data.get('downspeed', 0),  # 设备下载速度(B/s)
                    'upspeed': data.get('upspeed', 0),  # 设备上传速度(B/s)
                    'online': data.get('online', 0)
                })
            return devices
        except Exception as e:
            RouterLogger.log_error("获取设备列表失败", e)
