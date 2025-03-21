# 小米路由器 API 文档

-----

> 原作者:"[azwhikaru](https://github.com/azwhikaru)"因本人已不再使用小米路由器，所以本文档无限期搁置中... 欢迎大佬 Fork 之后继续扒 API
>
> api调用实例参考项目,[Mirouterui](https://github.com/Mirouterui/mirouter-ui)
>
> 本项目介绍,python重构,其实Mirouterui已经很全面了,我就是有点闲.



```
'R1D': '小米路由器',
'R2D': '小米路由器2',
'R3D': '小米路由器HD',

'R1CM': '小米路由器MINI',
'R1CL': '小米路由器青春版',

'R3': '小米路由器3',
'R3A': '小米路由器3A',
'R3D': '小米路由器HD',
'R3L': '小米路由器3C',
'R3P': '小米路由器3 Pro',
'R3G': '小米路由器3G',
'R3Gv2': '小米路由器3G v2',

'R4': '小米路由器4',
'R4A': '小米路由器4 千兆版',
'R4Av2': '小米路由器4A 千兆版',
'R4AC': '小米路由器4A',
'R4C': '小米路由器4Q',
'R4CM': '小米路由器4C',

'R1500': '小米路由器1500',
'R1350': '小米路由器4 Pro',
'R1800': '小米AIoT路由器 AX1800',
'R2100': '小米路由器 AC2100',
'R2350': '小米路由器 AC2350',
'R2600': '小米路由器 2600',
'R3600': '小米AIoT路由器 AX3600',

'RA50': 'Redmi路由器 AX5 京东云无线宝',
'RA67': 'Redmi路由器 AX5',
'RA67U': '小米路由器 AX1800',
'RA69': 'Redmi路由器 AX6',
'RA70': '小米路由器 AX9000',
'RA71': '小米路由器 AX1800',
'RA72': '小米路由器 AX6000',
'RA74': 'Redmi路由器 AX5400',
'RA80': '小米路由器 AX3000',
'RA80V2': '小米路由器 AX3000',
'RA81': 'Redmi路由器 AX3000',
'RA82': 'Xiaomi Mesh System AX3000',

'RB03': '小米路由器 AX6S'
'RB04': 'Redmi电竞路由器 AX5400'
'RB06': 'Redmi路由器 AX6000',
'RB08': 'Xiaomi HomeWiFi',

'RC01': 'Xiaomi万兆路由器',
'RC02': 'Xiaomi路由器AX3000 NE',
'RC06': 'Xiaomi路由器BE7000',

'RD01': 'Xiaomi全屋路由',
'RD02': 'Xiaomi全屋路由 子路由',
'RD03': 'Xiaomi路由器 AX3000T',
'RD04': 'Xiaomi路由器 AX1500',
'RD05': 'Xiaomi路由器4A 千兆版',
'RD08': 'Xiaomi路由器 BE6500 Pro',
'RD12': 'Xiaomi路由器 AX1500',
'RD13': 'Xiaomi Mesh System AC1200',
'RD15': 'Xiaomi路由器 BE3600 2.5G版',
'RD16': 'Xiaomi路由器 BE3600',
'RD18': 'Xiaomi路由器 BE5000',
'RD23': 'Xiaomi路由器 AX300T',
'RD28': 'Xiaomi Mesh System AX3000 NE',

"RN01": 'Xiaomi路由器 BE3600Pro'
"RN02": 'Xiaomi路由器 BE6500'
"RN04": 'Xiaomi路由器 BE3600Pro'
"RN06": 'Xiaomi路由器 BE3600'
"RN07": 'Xiaomi路由器 AX3000E'

'RM015': '小米路由器',
'RM1800': '小米路由器 AX1800',
'RM2100': '小米路由器 AC2100',

'old15': '小米路由器',

'R1D': 'Redmi路由器',
'R2D': 'Redmi路由器2',


'V1': '小米路由器',
'V2': '小米路由器',
'V3': '小米路由器3',

'LV1': '小米路由器青春版',
'LV3': '小米路由器R3C',

'MV1': '小米路由器mini',

'MR30U': '小米路由器WR30U',

'D01': '小米路由器Mesh',

'CR5508': '小米路由器CR5508',
'CR6606': '小米路由器CR6606',
'CR8806': '小米路由器CR8806',
'CR8808': '小米路由器CR8808',
'CR8809': '小米路由器CR8809',
'CR8816': '小米路由器CR8816',

'TR606': '小米路由器TR606',
```



-----

## 1. 登录

**调用地址**: `/api/xqsystem/login`  

```
http://{ip}/cgi-bin/luci/api/xqsystem/login

params = {
    "username": "admin",
    "password": 密码,
    "logtype": "2",  # 新增必要参数
    "nonce": nonce

}
```

```
key = 'a2ffa5c9be07488bbb04a3a47d3c5f6a'
```



**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
username | `True` | admin | 无
password | `True` | 无 | 需要加密(新:SHA256两次哈希,旧:SHA1两次哈希) 
nonce | `True` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
url | 指向后台管理的主页 | 无 |
token | 即 `stok` | 无 |

```
```



-----

## 2. 获取初始化信息

**调用地址**: `/api/xqsystem/init_info`  

**必须 Token**: `False`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
isSupportMesh | 是否支持 Mesh | `1.True  0.False` |
secAcc | 未知 | `1.True  0.False`|
inited | 已初始化 | `1.True  0.False` |
connect | 未知 | `1.True  0.False` |
modules | 未知 | `1.True  0.False` |
replacement_assistant | 未知 | `1.True  0.False` |
hardware | 硬件 | 当前硬件 |
language | 系统语言 | 当前系统语言 |
romversion | 固件版本 | 当前固件版本 |
countrycode | 国家代码 | 当前国家代码 |
id | 路由器序列号 | 当前路由器序列号 |
routername | 路由器名称 | 当前路由器名称 |
displayName | 显示名称 | 当前显示名称 |
maccel | 未知 | `1.True  0.False` |
model | 机型 | 当前机型 |
DisableTencent | 未知 | `1.True  0.False` |
bound | 未知 | `1.True  0.False` |
routerId | 设备 ID | 当前路由器的设备 ID (米家) |
isRedmi | 是否为 Redmi | `1.True  0.False` |

```json
{
    "features": {
        "netmode": {
            "elink": "0",
            "net2.5G": "0"
        },
        "hardware": {
            "disk": "0",
            "usb_deploy": "0",
            "usb": "0"
        },
        "wifi": {
            "twt": "1",
            "wifi24": "1",
            "wifi50": "1",
            "wifiguest": "1",
            "wifimerge": "1",
            "wifi_mu_mimo": "0"
        },
        "apps": {
            "mipctlv2": "1",
            "apptc": "0",
            "timemachine": "0",
            "LED_control": "1",
            "wanLan": "1",
            "swapmask": "0",
            "game_port": "0",
            "nfc": "0",
            "dhcpMsg": "1",
            "lanPort": "1",
            "local_gw_security": "1",
            "ports_custom": "1",
            "firewall": "1",
            "xqdatacenter": "1",
            "upnp": "1",
            "download": "0",
            "qos": "1",
            "lan_lag": "1"
        },
        "apmode": {
            "lanapmode": "1",
            "wifiapmode": "1"
        },
        "system": {
            "multiwan": "1",
            "downloadlogs": "0",
            "ipv6_wired": "0",
            "i18n": "0",
            "ipv6_wired_v2": "1",
            "mesh_bhtype_mode": "1",
            "infileupload": "1",
            "ipv6_passthrough_relay": "1",
            "set_router_location": "0",
            "shutdown": "0",
            "upnp": "1",
            "support_1000_dhcp": "1",
            "task": "0",
            "new_update": "1"
        }
    },
    "code": 0,
    "isSupportMesh": 1,
    "secAcc": 1,
    "inited": 1,
    "connect": 0,
    "routerId": "3b4ebd2f-15c9-430f-a7ec-831b3b03cce6",
    "ipv6": 1,
    "child_router": "0",
    "mesh_nodes": [],
    "hardware": "RN07",
    "support160M": 1,
    "miioVer": "2",
    "isRedmi": 0,
    "romversion": "1.0.24",
    "countrycode": "CN",
    "imei": "",
    "modules": {
        "replacement_assistant": "1"
    },
    "id": "58882/K4UZ18236",
    "routername": "Xiaomi_442F",
    "showPrivacy": 0,
    "displayName": "Xiaomi路由器AX3000E",
    "miioDid": "841194730",
    "moduleVersion": "",
    "maccel": "1",
    "model": "xiaomi.router.rn07",
    "wifi_ap": 1,
    "bound": 0,
    "newEncryptMode": 1,
    "language": "zh_cn"
}
```



-----

## 2.1.重启路由器

**调用地址**: `/api/xqsystem/reboot`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 返回值说明

参数名称 | 解释 | 值 
-|-|-
code | 状态码 | 0 
lanIp | IP地址 |      

```json
{
    "lanIp": [
        {
            "mask": "255.255.255.0",
            "ip": "192.168.31.1"
        }
    ],
    "code": 0
}
```

## 2.2.关机

**调用地址**: `/api/xqsystem/shutdown`  

**必须 Token**: `True`   

**请求方式**: `GET`

## 2.3.恢复出厂设置

**调用地址**: `/api/xqsystem/reset`  

**必须 Token**: `True`   

**请求方式**: `GET`



## 3. 获取工厂信息

**调用地址**: `/api/xqsystem/fac_info`  

**必须 Token**: `False`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
init | 是否初始化 | `1.True  0.False` |
wl0_ssid | 网卡 `wlan0` 上的 SSID | 当前 SSID |
wl1_ssid | 网卡 `wlan1` 上的 SSID | 当前 SSID |
telnet | 是否开启 Telnet | `1.True  0.False` |
ssh | 是否开启 SSH | `1.True  0.False` |
facmode | 是否为工厂模式 | `1.True  0.False` |
4kblock | 是否为 4K Block | `Boolean` |
secboot | 是否开启安全启动 | `Boolean` |
uart | 是否开启 UART | `Boolean` |

```json
{
    "telnet": false,
    "init": true,
    "wl0_ssid": "Xiaomi_442F_5G",
    "ssh": false,
    "version": "1.0.24",
    "facmode": false,
    "4kblock": false,
    "secboot": false,
    "wl1_ssid": "Xiaomi_442F",
    "uart": false
}
```

-----

## 4. Farewell (未知)

**调用地址**: `/api/xqsystem/farewell`  

**必须 Token**: `False`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |

```
{
    "code": 0
}
```



-----

## 5. 获取 Token 信息

**调用地址**: `/api/xqsystem/token`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
id | 路由器序列号 | 当前路由器序列号 |
name | 路由器名称 | 当前路由器名称 |
token | 即 `stok` | 无 |

-----

## 6. 设置 Init 状态

**调用地址**: `/api/xqsystem/set_inited`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
client | `False` | `ios, android, other` | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |

-----

## 7. 获取系统信息

**调用地址**: `/api/xqsystem/sys_info`  

**必须 Token**: `False`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
hardware | 硬件 | 当前硬件 |
routerName | 路由器名称 | 当前路由器名称 |
romVersion | 固件版本 | 当前固件版本 |
romChannel | 固件类型 | 当前固件类型 (`release.稳定版  stable.开发版  current.测试版`) |

-----

## 8. 置 Init 状态

**调用地址**: `/api/xqsystem/set_inited`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
client | `False` | `ios, android, other` | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |

-----

## 9. 设置密码

**调用地址**: `/api/xqsystem/set_name_password`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
nonce | `True` | 无 | 无
oldPwd | `True` | 无 | 旧的密码
newPwd | `True` | 无 | 要设置的密码

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
msg | 状态信息 | 状态信息 (如果有) |

-----

## 10. 检查固件更新

**调用地址**: `/api/xqsystem/check_rom_update`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
needUpdate | 是否需要更新 | `1.True  0.False` |
changeLog | 新版本更新日志 | 新版本更新日志 |
version | 最新版本 | 当前最新版本 |
status - status | 未知 | 未知 |
status - percent | 未知 | 未知 |

```
{
    "needUpdate": 0,
    "code": 0,
    "status": {
        "status": 0,
        "percent": 0
    },
    "changeLog": "",
    "version": "1.0.24"
}
```



-----

## 11. WAN、LAN 口状态

**调用地址**: `/api/xqsystem/lan_wan`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 
-|-|-
code | 状态码 | 0 
downspeed | 当前下载速度 | 当前下载速度 (Bit/s) 
maxdownloadspeed | 最高下载速度 | 最高下载速度 (Bit/s) 
download | 已下载的数据量 | 已下载的数据量 (Bit) 
upspeed | 当前上传速度 | 当前上传速度 (Bit/s) 
maxuploadspeed | 最高上传速度 | 最高上传速度 (Bit/s) 
upload | 已上传的数据量 | 已上传的数据量 (Bit) 
devname | 接口名称 | WAN/LAN 口对应的接口名称 

```
{
    "wan": {
        "downspeed": "3482",
        "maxdownloadspeed": "64986784",
        "devname": "nil",
        "upload": "21813019663",
        "upspeed": "4423",
        "maxuploadspeed": "14842495",
        "download": "61155655557"
    },
    "lan": {
        "downspeed": "0",
        "maxdownloadspeed": "0",
        "devname": "",
        "upload": "0",
        "upspeed": "0",
        "maxuploadspeed": "0",
        "download": "0"
    },
    "code": 0
}
```



-----

## 12. 刷入固件

**调用地址**: `/api/xqsystem/flash_rom`  

**必须 Token**: `True`   

**请求方式**: `GET`   

**备注**: 刷入位于事先上传的固件

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
msg | 状态信息 | 状态信息 (如果有) |

-----

## 13. 获取路由器名称

**调用地址**: `/api/xqsystem/router_name`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
routerName | 路由器名称 | 当前路由器名称 |

```
{
    "routerName": "Xiaomi_442F",
    "code": 0
}
```



-----

## 14. 获取设备列表

**调用地址**: `/api/xqsystem/device_list`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
all | `False` | 0 | `1.显示所有连接过的设备  0.显示当前连接的设备`

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
mac | MAC 地址 | 用作请求的设备 / List 成员的设备的 MAC 地址 |
isap | 是否为 AP | `1.True  0.False` |
parent | 未知 | 未知 |
port | 端口 | 未知 |
hostname | 主机名 | 设备的主机名 |
mac | MAC 地址 | 设备的 MAC 地址 |
origin_name | 原始名称 | 设备的原始名称 |
ptype | 未知 | 未知 |
authority - wan | 可访问 `wan` 网络 | `1.True  0.False` |
authority - lan | 可访问 `lan` 网络 | `1.True  0.False` |
authority - admin | 可以管理员身份访问 | `1.True  0.False` |
authority - pridisk | 可访问隐私盘 (如果支持挂载磁盘) | `1.True  0.False` |
company - priority | 未知 | 未知 |
company - type | 未知 | 未知 |
company - type - p | 未知 | 未知 |
company - type - c | 未知 | 未知 |
company - name | 制造商名称 | 设备的制造商名称 |
company - icon | 制造商 Logo | 设备巅峰制造商 Logo |
push | 未知 | 未知 |
name | 名称 | 设备的名称 (自定义) |
times | 未知 | 未知 |
type | 连接方式 | 设备连接方式 (`line.有线连接  wifi.无线连接`) |
statistics - mac | MAC 地址 | 设备的 MAC 地址 |
statistics - ip | DHCP IP 地址 | 设备的 DHCP IP 地址 |
statistics - online | 已在线时长 | 设备的已在线时长 (秒) |
statistics - downspeed | 当前下载速度 | 设备当前下载速度 (Bit/s) |
statistics - maxdownloadspeed | 最大下载速度 | 设备最大下载速度 (Bit/s) |
statistics - download | 已下载的数据量 | 设备已下载的数据量 (Bit) |
statistics - upspeed | 当前上传速度 | 设备当前上传速度 (Bit/s) |
statistics - maxuploadspeed | 最大上传速度 | 设备最大上传速度 (Bit/s) |
statistics - upload | 已上传的数据量 | 设备已上传的数据量 (Bit) |
ctype | 未知 | 未知 |
online | 是否在线 | 设备当前是否在线 (`1.True  0.False`) |

```
{
    "mac": "76:2B:C7:15:73:26",
    "list": [
        {
            "isap": 0,
            "parent": "",
            "ip": "192.168.31.179",
            "port": 2,
            "hostname": "odRoWvgK-deRedmi-K70-Ultra",
            "mac": "DE:A5:13:B2:5A:A2",
            "origin_name": "odRoWvgK-deRedmi-K70-Ultra",
            "ptype": 0,
            "authority": {
                "wan": 1,
                "pridisk": 0,
                "admin": 1,
                "lan": 1
            },
            "company": {
                "priority": 2,
                "type": {
                    "p": 0,
                    "c": 0,
                    "n": ""
                },
                "name": "",
                "icon": ""
            },
            "push": 0,
            "name": "odRoWvgK-deRedmi-K70-Ultra",
            "times": 0,
            "type": "wifi",
            "statistics": {
                "mac": "DE:A5:13:B2:5A:A2",
                "maxdownloadspeed": "1936148",
                "upload": "31897675",
                "upspeed": "0",
                "ip": "192.168.31.179",
                "downspeed": "0",
                "online": "14883",
                "dev": "wl0",
                "maxuploadspeed": "327414",
                "download": "214408540"
            },
            "ctype": 0,
            "online": 1
        },
        {
            "isap": 0,
            "parent": "",
            "ip": "192.168.31.55",
            "port": 2,
            "hostname": "iQOO-Neo9S-Pro",
            "mac": "86:85:D6:D5:BD:FD",
            "origin_name": "iQOO-Neo9S-Pro",
            "ptype": 0,
            "authority": {
                "wan": 1,
                "pridisk": 0,
                "admin": 1,
                "lan": 1
            },
            "company": {
                "priority": 2,
                "type": {
                    "p": 0,
                    "c": 0,
                    "n": ""
                },
                "name": "",
                "icon": ""
            },
            "push": 0,
            "name": "iQOO-Neo9S-Pro",
            "times": 0,
            "type": "wifi",
            "statistics": {
                "mac": "86:85:D6:D5:BD:FD",
                "maxdownloadspeed": "64986247",
                "upload": "2441183822",
                "upspeed": "4230",
                "ip": "192.168.31.55",
                "downspeed": "2191",
                "online": "58816",
                "dev": "wl0",
                "maxuploadspeed": "2052774",
                "download": "17052869220"
            },
            "ctype": 0,
            "online": 1
        },
        {
            "isap": 0,
            "parent": "",
            "ip": "192.168.31.197",
            "port": 2,
            "hostname": "*",
            "mac": "76:2B:C7:15:73:26",
            "origin_name": "",
            "ptype": 0,
            "authority": {
                "wan": 1,
                "pridisk": 0,
                "admin": 1,
                "lan": 1
            },
            "company": {
                "priority": 2,
                "type": {
                    "p": 0,
                    "c": 0,
                    "n": ""
                },
                "name": "",
                "icon": ""
            },
            "push": 0,
            "name": "76:2B:C7:15:73:26",
            "times": 0,
            "type": "wifi",
            "statistics": {
                "mac": "76:2B:C7:15:73:26",
                "maxdownloadspeed": "3466858",
                "upload": "21293225",
                "upspeed": "0",
                "ip": "192.168.31.197",
                "downspeed": "0",
                "online": "11893",
                "dev": "wl0",
                "maxuploadspeed": "242419",
                "download": "441041759"
            },
            "ctype": 0,
            "online": 1
        },
        {
            "isap": 0,
            "parent": "",
            "ip": "192.168.31.196",
            "port": 2,
            "hostname": "Xiaomi-Pad-6-Pro",
            "mac": "A2:4C:4A:AF:6B:17",
            "origin_name": "Xiaomi-Pad-6-Pro",
            "ptype": 0,
            "authority": {
                "wan": 1,
                "pridisk": 0,
                "admin": 1,
                "lan": 1
            },
            "company": {
                "priority": 2,
                "type": {
                    "p": 0,
                    "c": 0,
                    "n": ""
                },
                "name": "",
                "icon": ""
            },
            "push": 0,
            "name": "Xiaomi-Pad-6-Pro",
            "times": 0,
            "type": "wifi",
            "statistics": {
                "mac": "A2:4C:4A:AF:6B:17",
                "maxdownloadspeed": "4570896",
                "upload": "7054214",
                "upspeed": "0",
                "ip": "192.168.31.196",
                "downspeed": "0",
                "online": "161118",
                "dev": "wl0",
                "maxuploadspeed": "173751",
                "download": "125954962"
            },
            "ctype": 0,
            "online": 1
        }
    ],
    "code": 0
}
```



-----

## 15. 设置设备名称

**调用地址**: `/api/xqsystem/set_device_nickname`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
mac | `True` | 无 | 要修改名称的设备的 MAC 地址
name | `True` | 无 | 要设置的名称
owner | `False` | 无 | 未知
device | `False` | 无 | 未知

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
msg | 状态信息 | 状态信息 (如果有) |

-----

## 16. 是否联网成功

**调用地址**: `/api/xqsystem/internet_connect`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
connect | 联网状态 | `0.True  1.False` |

```
{
    "connect": 0,
    "code": 0
}
```



-----

## 17. 上传 ROM 文件 ([参见: 刷入固件](#刷入固件))

**调用地址**: `/api/xqsystem/upload_rom`  

**必须 Token**: `True`   

**请求方式**: `POST / PUT`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
UPLOADFILE | `True` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
msg | 状态信息 | 状态信息 (如果有) |
downgrade | 是否为降级固件 | `Boolean`

-----

## 18. 获取可用语言

**调用地址**: `/api/xqsystem/get_languages`  

**必须 Token**: `False`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
list - lang | 可用语言代码 | 可用语言代码 |
list - name | 可用语言 | 可用语言 |
lang | 当前语言 | 当前语言 |

```
{
    "list": [
        {
            "lang": "zh_cn",
            "name": "简体中文"
        }
    ],
    "lang": "zh_cn",
    "code": 0
}
```



-----

## 19. 获取当前语言

**调用地址**: `/api/xqsystem/get_main_language`  

**必须 Token**: `False`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
lang | 当前语言代码 | 当前语言代码 |

```
{
    "lang": "zh_cn",
    "code": 0
}
```



-----

## 20. 设置语言

**调用地址**: `/api/xqsystem/set_language`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
language | `True` | 无 | 语言代码

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
msg | 状态信息 | 状态信息 (如果有) |

-----

## 21. 上传日志

**调用地址**: `/api/xqsystem/upload_log`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
msg | 状态信息 | 状态信息 (如果有) |

-----

## 22. 设置基本信息 (初始化)

**调用地址**: `/api/xqsystem/router_init`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
nonce | `True` | 无 | 无
newPwd | `True` | 无 | 新的密码
oldPwd | `True` | 无 | 旧的密码
wifiPwd | `True` | 无 | WiFi 密码
wifi24Ssid | `True` | 无 | 2.4Ghz WiFi SSID
wifi50Ssid | `True` | 无 | 5Ghz WiFi SSID
wanType | `True` | 无 | `wan` 类型 `(pppoe.拨号  dhcp.自动获取)`
pppoeName | `False` | 无 | 宽带账号
pppoePwd | `False` | 无 | 宽带密码

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
msg | 状态信息 | 状态信息 (如果有) |

-----

## 23. 获取详细信息

**调用地址**: `/api/xqsystem/information`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 |
-|-|-|
code | 状态码 | 0 |
connect | 联网状态 | `0.True  1.False` |
wifi - ifname | 接口内部名称 | `WiFi` 接口的内部名称 |
wifi - channelInfo - bandwidth | 频段带宽 | `WiFi` 的频段带宽 |
wifi - channelInfo - bandList | 可用频段带宽 | `WiFi` 可用的频段带宽 |
wifi - channelInfo - channel | 信道 | `WiFi` 的信道 |
wifi - encryption | 加密方式 | `WiFi` 的加密方式 |
wifi - bandwidth | 频段带宽 | `WiFi` 的频段带宽 |
wifi - kickthreshold | RSSI | `WiFi` 的RSSI 数值 |
wifi - status | 启用状态 | `WiFi` 是否启用 `(1.True  0.False)` |
wifi - mode | 模式 | `WiFi` 模式 `(参考 OpenWrt 的 Master、Bridge)` |
wifi - bsd | 未知 | 未知 |
wifi - ssid | SSID | `WiFi` 的 SSID |
wifi - weakthreshold | 保护阈值 | 未知 |
wifi - device | 设备 | `WiFi` 使用的设备 |
wifi - ax | 802.11ax | `WiFi` 是否启用 802.11ax `(1.True  0.False)` |
wifi - hidden | 隐藏 SSID | `WiFi` 是否隐藏 SSID `(1.True  0.False)` |
wifi - password | WiFi 密码 | `WiFi` 的 WiFi 密码 |
wifi - channel | 信道 | `WiFi` 的信道 |
wifi - txpwr | 发射功率 | `WiFi` 发射功率 `(max.穿墙  mid.标准  min.节能)` |
wifi - weakenable | 未知 | 未知 |
wifi - txbf | BeamForming | `WiFi` 波束成形波数 `(3.启用 BeamForming  0.关闭 BeamForming)` |
wan - mac | MAC 地址 | `wan` 口的 MAC 地址 |
wan - link | 线路数量 | `wan` 口连接的线路数量 |
wan - details - username | PPPOE 用户名 | `wan` 口的 PPPOE 用户名 |
wan - details - password |  PPPOE 密码 | `wan` 口的 PPPOE 密码 |
wan - special | 特殊拨号 | `wan` 口是否使用特殊拨号 `(1.True  0.False)` |
wan - details - ifname | 内部名称 | 内部名称 |
wan - details - wanType | 无 | `wan` 类型 `(pppoe.拨号  dhcp.自动获取)`
wan - details - mru |  Maximum Receive Unit | `wan` 口的最大接收单元 |
wan - mtu | Maximum Transmission Unit | `wan` 口的最大传输单元 |
wan - details - service |  未知 | 未知 |
wan - details - peerdns |  PeerDNS | `wan` 口的 PeerDNS `(1.True  0.False)` |
wan - status | 启用状态 | `wan` 口的启用状态 `(1.True  0.False)` |
wan - dnsAddrs | DNS 1 | `wan` 口的 DNS 1 |
wan - dnsAddrs1 | DNS 2 | `wan` 口的 DNS 2 |
wan - uptime | 已在线时长 | `wan` 口的已在线时长 (秒) |
wan - gateWay | 网关 | `wan` 口的网关 |
wan - ipv6_info - ifname | IPv6 内部名称 | IPv6 的内部名称 |
wan - ipv6_info - lan_ip6addr | LAN IPv6 地址 | LAN IPv6 地址 |
wan - ipv6_info - lan_ip6prefix | LAN IPv6 前缀 | LAN IPv6 前缀 |
wan - ipv6_info - peerdns | PeerDNS | IPv6 的 PeerDNS `(1.True  0.False)` |
wan - ipv6_info - wanType | IPv6 连接类型 | IPv6 连接类型 |
wan - ipv6_info - ip6addr | WAN IPv6 地址 | WAN IPv6 地址 |
wan - ipv4 - ip | WAN IPv4 地址 | WAN IPv4 地址 |
wan - ipv6_info - dns | IPv6 DNS 地址 | IPv6 DNS 地址 |
wan - ipv6_info - dns_conf | IPv6 DNS 地址 | IPv6 DNS 地址 |
wan - ipv6_show | 显示 IPv6 选项 | 显示 IPv6 选项 `(1.True  0.False)` |
wan - ipv4 - mask | 子网掩码 | 子网掩码 |
lan - mac | MAC 地址 | `lan` 口的 MAC 地址 |
lan - uptime | 已在线时长 | `lan` 口的已在线时长 (秒) |
lan - status | 启用状态 | `lan` 口的启用状态 `(1.True  0.False)` |
lan - dnsAddrs | DNS 1 | `lan` 口的 DNS 1 |
lan - dnsAddrs1 | DNS 2 | `lan` 口的 DNS 2 |
lan - ipv4 - mask | LAN 子网掩码 | LAN 子网掩码 |
lan - ipv4 - ip | LAN IPv4 地址 | LAN IPv4 地址 |

```
{
    "lan": {
        "status": 1,
        "mac": "58:EA:1F:CD:10:BC",
        "uptime": 162322,
        "ipv4": [
            {
                "mask": "255.255.255.0",
                "ip": "192.168.31.1"
            }
        ]
    },
    "wan": {
        "mac": "44:F7:70:7F:44:2F",
        "link": 1,
        "details": {
            "wanType": "dhcp",
            "peerdns": "1",
            "ifname": "eth0.1",
            "mtu": "1500"
        },
        "gateWay": "192.168.71.1",
        "dnsAddrs1": "180.168.255.18",
        "mtu": "1500",
        "uptime": 162285,
        "ipv6_info": {
            "ifname": "eth0.1",
            "lan_ip6addr": [
                [
                    "240e:38b:8758:300:5aea:1fff:fecd:10bc/64"
                ]
            ],
            "ipv6_mode": "pi_relay",
            "peerdns": "1",
            "wanType": "pi_relay",
            "ip6addr": [
                "240e:38b:8758:300:46f7:70ff:fe7f:442f/64"
            ],
            "dns": [],
            "ip6gw": "fe80::247:7cc9:26ef:534",
            "lan_ip6prefix": [
                "240e:38b:8758:300::"
            ],
            "up": true
        },
        "status": 1,
        "ipv6_show": 1,
        "dnsAddrs": "116.228.111.118",
        "ipv4": [
            {
                "mask": "255.255.255.0",
                "ip": "192.168.71.12"
            }
        ]
    },
    "code": 0,
    "wifi": [
        {
            "ifname": "wl1",
            "channelInfo": {
                "bandwidth": "0",
                "bandList": [
                    "20",
                    "40"
                ],
                "channel": "0"
            },
            "encryption": "psk2",
            "wifimode": "11ax",
            "bandwidth": "0",
            "kickthreshold": "0",
            "status": "0",
            "mode": "Master",
            "bsd": "0",
            "ssid": "Xiaomi_442F",
            "weakthreshold": "0",
            "device": "wifi0.network1",
            "ax": "1",
            "hidden": "0",
            "password": "123w45678",
            "weakenable": "0",
            "ssid_len_limit": "28",
            "channel": "",
            "txpwr": "min",
            "txbf": "3",
            "available_channels": [
                {
                    "c": 0,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 1,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 2,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 3,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 4,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 5,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 6,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 7,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 8,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 9,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 10,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 11,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 12,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 13,
                    "b": [
                        "20",
                        "40"
                    ]
                }
            ],
            "signal": 0
        },
        {
            "ifname": "wl0",
            "channelInfo": {
                "bandwidth": "0",
                "bandList": [
                    "20",
                    "40",
                    "80",
                    "160"
                ],
                "channel": 40
            },
            "encryption": "psk2+ccmp",
            "wifimode": "11ax",
            "bandwidth": "0",
            "kickthreshold": "0",
            "status": "1",
            "mode": "Master",
            "bsd": "0",
            "ssid": "Xiaomi_442F_5G",
            "weakthreshold": "0",
            "device": "wifi1.network1",
            "ax": "1",
            "hidden": "0",
            "password": "123w45678",
            "weakenable": "0",
            "ssid_len_limit": "31",
            "channel": "40(20M)",
            "txpwr": "max",
            "txbf": "3",
            "available_channels": [
                {
                    "c": 0,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 36,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 40,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 44,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 48,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 52,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 56,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 60,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 64,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 149,
                    "b": [
                        "20",
                        "40",
                        "80"
                    ]
                },
                {
                    "c": 153,
                    "b": [
                        "20",
                        "40",
                        "80"
                    ]
                },
                {
                    "c": 157,
                    "b": [
                        "20",
                        "40",
                        "80"
                    ]
                },
                {
                    "c": 161,
                    "b": [
                        "20",
                        "40",
                        "80"
                    ]
                },
                {
                    "c": 165,
                    "b": [
                        "20"
                    ]
                }
            ],
            "signal": -95
        }
    ],
    "connect": 0
}
```



------

## 24. 获取路由器状态

**调用地址**: `/api/misystem/status`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
无 | `False` | 无 | 无

### 返回值说明

参数名称 | 解释 | 值 
-|-|-
code | 状态码 | 0 
 dev         | 设备列表     | 数组 
mem | 内存状态     | 数组                   
temperature | 温度 | 若没有温度传感器则为0 
count | 连接设备计数 | 数组 
hardware | 路由器信息 | 数组 
upTime | 在线时长 | 路由器的运行时间（秒） 
cpu | cpu信息 | 数组 
wan | `wan`口数据 | 数组 

#### dev数组

> 内有多个数组

| 参数名称         | 解释         | 值                           |
| ---------------- | ------------ | ---------------------------- |
| mac              | mac          | 设备mac地址                  |
| maxdownloadspeed | 最大下载速度 | 数字（B/S）                  |
| upload           | 总上传量     | 数字（B）                    |
| upspeed          | 上传速度     | 数字（B/S）                  |
| downspeed        | 下载速度     | 数字（B/S）                  |
| online           | 在线时长     | 数字（S）                    |
| devname          | 设备名称     | 所连接设备的名称（自定义后） |
| maxuploadspeed   | 最大上传速度 | 数字（B/S）                  |
| download         | 总下载量     | 数字（B）                    |

#### mem数组

| 参数名称 | 解释     | 值                       |
| -------- | -------- | ------------------------ |
| usage    | 内存占用 | 小数（eg:**0.5**）       |
| total    | 内存大小 | 字符串（eg:**128MB**）   |
| hz       | 内存频率 | 字符串（eg:**1200MHz**） |
| type     | 内存类型 | 字符串（eg:**DDR3**）    |

#### count数组

| 参数名称 | 解释               | 值   |
| -------- | ------------------ | ---- |
| all      | 连接过的设备数量   | 数字 |
| online   | 当前在线的设备数量 | 数字 |

#### hardware数组

| 参数名称 | 解释           | 值     |
| -------- | -------------- | ------ |
| mac      | 路由器MAC地址  | 字符串 |
| platform | 路由器型号     | 字符串 |
| version  | 路由器系统版本 | 字符串 |
| channel  | 路由器发行版本 | 字符串 |
| sn       | 路由器**sn**码 | 字符串 |

#### cpu数组

| 参数名称 | 解释      | 值     |
| -------- | --------- | ------ |
| core     | CPU核心数 | 数字   |
| hz       | CPU频率   | 字符串 |
| load     | CPU占用   | 小数   |

#### wan数组

| 参数名称         | 解释                              | 值     |
| ---------------- | --------------------------------- | ------ |
| downspeed        | `wan`口的下载速度                 | 数字   |
| maxdownloadspeed | `wan`口的最大下载速度             | 数字   |
| history          | `wan`口的上下行速度之和的历史记录 | 数组   |
| devname          | `wan`口设备名称                   | 字符串 |
| upload           | `wan`口总上传量                   | 数字   |
| upspeed          | `wan`口的下载速度                 | 数字   |
| maxuploadspeed   | `wan`口的最大上传速度             | 数字   |
| download         | `wan`口的最大下载                 | 数字   |

##### history数组

​	有50个数字，表示速度（B/S）

```
{
    "dev": [
        {
            "mac": "A0:E7:0B:FF:7B:ED",
            "maxdownloadspeed": "57919198",
            "isap": 0,
            "upload": "550873553",
            "upspeed": "0",
            "downspeed": "0",
            "online": "0",
            "devname": "SCP-LSP",
            "maxuploadspeed": "12025539",
            "download": "19289131483"
        },
        {
            "mac": "86:85:D6:D5:BD:FD",
            "maxdownloadspeed": "64986247",
            "isap": 0,
            "upload": "2441856060",
            "upspeed": "966",
            "downspeed": "1057",
            "online": "59011",
            "devname": "iQOO-Neo9S-Pro",
            "maxuploadspeed": "2052774",
            "download": "17059112323"
        },
        {
            "mac": "B2:54:4C:53:6B:99",
            "maxdownloadspeed": "2440191",
            "isap": 0,
            "upload": "28239769",
            "upspeed": "0",
            "downspeed": "0",
            "online": "0",
            "devname": "HUAWEI_P30_Pro-b97f7f7223",
            "maxuploadspeed": "42317",
            "download": "1971920919"
        },
        {
            "mac": "76:2B:C7:15:73:26",
            "maxdownloadspeed": "3466858",
            "isap": 0,
            "upload": "21308901",
            "upspeed": "0",
            "downspeed": "0",
            "online": "12087",
            "devname": "76:2B:C7:15:73:26",
            "maxuploadspeed": "242419",
            "download": "441057801"
        },
        {
            "mac": "DE:A5:13:B2:5A:A2",
            "maxdownloadspeed": "1936148",
            "isap": 0,
            "upload": "31898410",
            "upspeed": "0",
            "downspeed": "0",
            "online": "15077",
            "devname": "odRoWvgK-deRedmi-K70-Ultra",
            "maxuploadspeed": "327414",
            "download": "214408672"
        },
        {
            "mac": "A2:4C:4A:AF:6B:17",
            "maxdownloadspeed": "4570896",
            "isap": 0,
            "upload": "7054318",
            "upspeed": "0",
            "downspeed": "0",
            "online": "161313",
            "devname": "Xiaomi-Pad-6-Pro",
            "maxuploadspeed": "173751",
            "download": "125955094"
        },
        {
            "mac": "B4:2E:99:15:A0:A9",
            "maxdownloadspeed": "346207",
            "isap": 0,
            "upload": "4784596",
            "upspeed": "0",
            "downspeed": "0",
            "online": "0",
            "devname": "DESKTOP-EMPNT2O",
            "maxuploadspeed": "605928",
            "download": "10432341"
        },
        {
            "mac": "90:2A:EE:00:5C:73",
            "maxdownloadspeed": "0",
            "isap": 0,
            "upload": "0",
            "upspeed": "0",
            "downspeed": "0",
            "online": "0",
            "devname": "ljredmig",
            "maxuploadspeed": "0",
            "download": "0"
        }
    ],
    "code": 0,
    "mem": {
        "usage": 0.6,
        "total": "256MB",
        "hz": "1333MHz",
        "type": "DDR3"
    },
    "temperature": 0,
    "count": {
        "all_without_mash": 15,
        "online": 4,
        "all": 15,
        "online_without_mash": 4
    },
    "hardware": {
        "mac": "44:F7:70:7F:44:2F",
        "platform": "RN07",
        "version": "1.0.24",
        "channel": "release",
        "ispName": "",
        "sn": "58882/K4UZ18236",
        "DisplayRomVer": "1.0.24",
        "displayName": "Xiaomi路由器AX3000E"
    },
    "upTime": "162390.93",
    "cpu": {
        "core": 2,
        "hz": "1000MHz",
        "load": 0
    },
    "wan": {
        "downspeed": "1057",
        "maxdownloadspeed": "64986784",
        "devname": "nil",
        "upload": "21814100377",
        "upspeed": "966",
        "maxuploadspeed": "14842495",
        "download": "61162418978"
    }
}
```



-----

## 25. 修改路由器名称

**调用地址**: `/api/xqsystem/set_router_name`  

**必须 Token**: `True`   

**请求方式**: `GET`   

### 参数说明

| 参数名称   | 必须   | 默认值 | 备注         |
| ---------- | ------ | ------ | ------------ |
| **locale** | `True` | 无     | 路由器新位置 |
| **name**   | `True` | 无     | 路由器新名称 |

### 返回值说明

| 参数名称 | 解释   | 值   |
| -------- | ------ | ---- |
| code     | 状态码 | 0    |

## 26.

**调用地址**: `/api/misystem/get_ps_map`  

**必须 Token**: `True`   

**请求方式**: `GET`



```
{
    "ports": [
        {
            "port": "1",
            "index": "1",
            "label": "LAN1",
            "speed": "1G",
            "service": "WAN"
        },
        {
            "port": "2",
            "index": "2",
            "label": "LAN2",
            "speed": "1G",
            "service": "LAN"
        },
        {
            "port": "3",
            "index": "3",
            "label": "LAN3",
            "speed": "1G",
            "service": "LAN"
        },
        {
            "port": "4",
            "index": "4",
            "label": "LAN4",
            "speed": "1G",
            "service": "LAN"
        }
    ],
    "description": "",
    "code": 0
}
```

## 27.

**调用地址**: `/api/misystem/messages`  

**必须 Token**: `True`   

**请求方式**: `GET`

```
{
    "messages": [],
    "count": 0,
    "code": 0
}
```

```
                var msgMap = {
                    '1': '<p>检测到最新版本为{$version}，<a href="/cgi-bin/luci/web/setting/upgrade">点击此处立即升级</a>。</p>',
                    '2': '<p>你有新短信，<a href="/cgi-bin/luci/web/prosetting/upnp">点击此处查看</a></p>',
                    '3': '<p>5G Wi-Fi启动失败，<a target="_blank" href="http://www.mi.com/service/contact/">请联系小米客服解决</a></p>',
                    '4': '<p>检测到与上级路由器存在IP冲突，建议切换到<a href="/cgi-bin/luci/web/setting/wan#netmode">有线中继模式</a>或者<a href="#" id="ipconflict" data-ip="{$ip}">避让IP冲突</a></p>',
                    '5': '<p>短信箱已满，<a href="/cgi-bin/luci/web/prosetting/upnp">请删除无用短信以保障短信功能正常</a></p>'
                };

                var msgMapD01 = {
                    '1': '<p>检测到最新版本为{$version}，<a href="/cgi-bin/luci/web/setting/upgrade">点击此处立即升级</a>。</p>',
                    '2': '<p>你有新短信，<a href="/cgi-bin/luci/web/prosetting/upnp">点击此处查看</a></p>',
                    '3': '<p>5G Wi-Fi启动失败，<a target="_blank" href="http://www.mi.com/service/contact/">请联系小米客服解决</a></p>',
                    '4': '<p>检测到与上级路由器存在IP冲突，请<a href="/cgi-bin/luci/web/setting/lannetset">修改局域网IP地址网段</a></p>',
                    '5': '<p>短信箱已满，<a href="/cgi-bin/luci/web/prosetting/upnp">请删除无用短信以保障短信功能正常</a></p>'
                };
```

## 28.避让IP冲突

**调用地址**: `/api/misystem/r_ip_conflict`  

**必须 Token**: `True`   

**请求方式**: `GET`

```
执行此操作，局域网IP将会变更为' + ip + '<br>' + '该过程无线网络会重启，将出现短暂掉线。
```

## 29.

**调用地址**: `/api/misystem/devicelist`  

**必须 Token**: `True`   

**请求方式**: `GET`

```
{
    "mac": "76:2B:C7:15:73:26",
    "list": [
        {
            "mac": "DE:A5:13:B2:5A:A2",
            "oname": "odRoWvgK-deRedmi-K70-Ultra",
            "isap": 0,
            "pctlv2": 0,
            "parent": "",
            "authority": {
                "wan": 1
            },
            "push": 0,
            "online": 1,
            "name": "odRoWvgK-deRedmi-K70-Ultra",
            "times": 0,
            "ip": [
                {
                    "downspeed": "0",
                    "online": "15836",
                    "active": 1,
                    "upspeed": "0",
                    "ip": "192.168.31.179"
                }
            ],
            "statistics": {
                "downspeed": "0",
                "online": "15836",
                "upspeed": "0"
            },
            "icon": "",
            "type": 2
        },
        {
            "mac": "76:2B:C7:15:73:26",
            "oname": "",
            "isap": 0,
            "pctlv2": 0,
            "parent": "",
            "authority": {
                "wan": 1
            },
            "push": 0,
            "online": 1,
            "name": "*",
            "times": 0,
            "ip": [
                {
                    "downspeed": "0",
                    "online": "12846",
                    "active": 1,
                    "upspeed": "0",
                    "ip": "192.168.31.197"
                }
            ],
            "statistics": {
                "downspeed": "0",
                "online": "12846",
                "upspeed": "0"
            },
            "icon": "",
            "type": 2
        },
        {
            "mac": "A2:4C:4A:AF:6B:17",
            "oname": "Xiaomi-Pad-6-Pro",
            "isap": 0,
            "pctlv2": 0,
            "parent": "",
            "authority": {
                "wan": 1
            },
            "push": 0,
            "online": 1,
            "name": "Xiaomi-Pad-6-Pro",
            "times": 0,
            "ip": [
                {
                    "downspeed": "0",
                    "online": "162071",
                    "active": 1,
                    "upspeed": "0",
                    "ip": "192.168.31.196"
                }
            ],
            "statistics": {
                "downspeed": "0",
                "online": "162071",
                "upspeed": "0"
            },
            "icon": "",
            "type": 2
        }
    ],
    "code": 0
}
```

## 30.

**调用地址**: `/api/misystem/topo_graph`  

**必须 Token**: `True`   

**请求方式**: `GET`

```
{
    "show": 0,
    "graph": {
        "ssid": "Xiaomi_442F",
        "color": 101,
        "ip": "192.168.31.1",
        "locale": "客厅",
        "name": "Xiaomi_442F",
        "channel": "release",
        "hardware": "RN07",
        "mode": 0,
        "renumber": 0,
        "onlines": "3"
    },
    "code": 0
}
```

31.

**调用地址**: `/api/xqnetwork/wifi_detail_all`  

**必须 Token**: `True`   

**请求方式**: `GET`

```
{
    "bsd": 0,
    "info": [
        {
            "ifname": "wl1",
            "channelInfo": {
                "bandwidth": "0",
                "bandList": [
                    "20",
                    "40"
                ],
                "channel": "0"
            },
            "encryption": "psk2",
            "wifimode": "11ax",
            "bandwidth": "0",
            "kickthreshold": "0",
            "status": "0",
            "mode": "Master",
            "bsd": "0",
            "ssid": "Xiaomi_442F",
            "weakthreshold": "0",
            "device": "wifi0.network1",
            "ax": "1",
            "hidden": "0",
            "password": "123w45678",
            "weakenable": "0",
            "ssid_len_limit": "28",
            "channel": "0",
            "txpwr": "min",
            "txbf": "3",
            "available_channels": [
                {
                    "c": 0,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 1,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 2,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 3,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 4,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 5,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 6,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 7,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 8,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 9,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 10,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 11,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 12,
                    "b": [
                        "20",
                        "40"
                    ]
                },
                {
                    "c": 13,
                    "b": [
                        "20",
                        "40"
                    ]
                }
            ],
            "signal": 0
        },
        {
            "ifname": "wl0",
            "channelInfo": {
                "bandwidth": "0",
                "bandList": [
                    "20",
                    "40",
                    "80",
                    "160"
                ],
                "channel": 40
            },
            "encryption": "psk2+ccmp",
            "wifimode": "11ax",
            "bandwidth": "0",
            "kickthreshold": "0",
            "status": "1",
            "mode": "Master",
            "bsd": "0",
            "ssid": "Xiaomi_442F_5G",
            "weakthreshold": "0",
            "device": "wifi1.network1",
            "ax": "1",
            "hidden": "0",
            "password": "123w45678",
            "weakenable": "0",
            "ssid_len_limit": "31",
            "channel": "0",
            "txpwr": "max",
            "txbf": "3",
            "available_channels": [
                {
                    "c": 0,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 36,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 40,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 44,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 48,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 52,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 56,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 60,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 64,
                    "b": [
                        "20",
                        "40",
                        "80",
                        "160"
                    ]
                },
                {
                    "c": 149,
                    "b": [
                        "20",
                        "40",
                        "80"
                    ]
                },
                {
                    "c": 153,
                    "b": [
                        "20",
                        "40",
                        "80"
                    ]
                },
                {
                    "c": 157,
                    "b": [
                        "20",
                        "40",
                        "80"
                    ]
                },
                {
                    "c": 161,
                    "b": [
                        "20",
                        "40",
                        "80"
                    ]
                },
                {
                    "c": 165,
                    "b": [
                        "20"
                    ]
                }
            ],
            "signal": -95
        }
    ],
    "code": 0
}
```

32.

**调用地址**: `/api/xqnetwork/wifi_detail_all`  

**必须 Token**: `True`   

**请求方式**: `GET`



添加mesh子节点



**调用地址**: `/api/xqnetwork/scan_mesh_node`  

**必须 Token**: `True`   

**请求方式**: `GET`

获取可添加的Mesh子节点

```
```

33.

**调用地址**: `/api/xqnetdetect/nettb2`  

**必须 Token**: `True`   

**请求方式**: `GET`

```
{
    "info": [
        {
            "wantype": "eth",
            "disabled": 0,
            "name": "wan",
            "error": 0,
            "wanname": "WAN1"
        },
        {
            "wantype": "eth",
            "disabled": 1,
            "name": "wan_2",
            "error": 1,
            "wanname": "WAN2"
        }
    ],
    "on": 0,
    "code": 0
}
```

34.

**调用地址**: `/api/misystem/get_ps_service`  

**必须 Token**: `True`   

**请求方式**: `GET`

参数名称 | 必须 | 默认值 | 备注
-|-|-|-
service | `True` | multiwan | 无

```
{
    "multiwan": {
        "enable": 0,
        "policy": {
            "bandwidth_wan1": "0",
            "currwan": "wan",
            "weight1": "1",
            "bandwidth_wan2": "0",
            "mode": 0,
            "weight2": "1"
        },
        "port_map": [
            {
                "name": "WAN1",
                "port": "1"
            },
            {
                "name": "WAN2",
                "port": "3"
            }
        ]
    },
    "code": 0
}
```

35.上网管理

**调用地址**: `/api/xqsystem/set_mac_filter`  

**必须 Token**: `True`   

**请求方式**: `GET`

| 参数名称 | 必须   | 默认值 | 备注 |
| -------- | ------ | ------ | ---- |
| mac      | `True` |        | 无   |

36

**调用地址**: `/api/xqnetwork/pppoe_status`  

**必须 Token**: `True`   

**请求方式**: `GET`

```
case 1 :
                            msg = '正在拨号...';
case 2 :
                            msg = '拨号成功';
case 3 :
                            msg = rsp.msg || '拨号失败';
                            msg = msg + '，正在尝试特殊拨号模式...';                            
case 4 :
                            msg = '已断开';
                            action = '<a id="pppoeStart" href="#">立即连接</a>';                            
                            
                            
                            
                            
```

37.

**调用地址**: `/api/xqnetwork/get_wan_status`  

**必须 Token**: `True`   

**请求方式**: `GET`



```
{
    "ipv6": {
        "code": 0,
        "wan6_info": {
            "ip6addr": [
                "240e:38b:8758:300:46f7:70ff:fe7f:442f/64"
            ],
            "ifname": "eth0.1",
            "dns": [],
            "up": true,
            "lan_ip6addr": [
                [
                    "240e:38b:8758:300:5aea:1fff:fecd:10bc/64"
                ]
            ],
            "ip6gw": "fe80::247:7cc9:26ef:534",
            "lan_ip6prefix": [
                "240e:38b:8758:300::"
            ],
            "ipv6_mode": "pi_relay"
        }
    },
    "code": 0,
    "ipv4": {
        "proto": "dhcp",
        "dns": [
            "116.228.111.118",
            "180.168.255.18"
        ],
        "code": 0,
        "status": 2,
        "wanSpeed": "1000",
        "gw": "192.168.71.1",
        "ip": {
            "mask": "255.255.255.0",
            "address": "192.168.71.12"
        }
    }
}
```

38.

**调用地址**: `/api/misystem/active`  

**必须 Token**: `True`   

**请求方式**: `GET`

39.

**调用地址**: `/api/xqdatacenter/request`  

**必须 Token**: `True`   

**请求方式**: `GET`

```
countryCode = 'cn'
{"api":642,"sleeptime":2,"country":"'+ countryCode +'"}
```





