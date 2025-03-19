import hashlib
import random
import time

import requests


def create_nonce():
    """模拟Go的createNonce函数生成随机nonce"""
    type_var = 0
    device_id = "6c:4b:90:c6:da:0e"  # 无用
    time_var = int(time.time())
    random_var = random.randint(0, 9999)
    return f"{type_var}_{device_id}_{time_var}_{random_var}"


def hash_password(pwd: str, nonce: str, key: str, encrypt_mode: bool = False) -> str:
    if encrypt_mode:
        # 新加密模式（SHA256两次哈希）
        pwd_key = pwd + key
        pwd_hash = hashlib.sha256(pwd_key.encode("utf-8")).hexdigest()
        return hashlib.sha256((nonce + pwd_hash).encode("utf-8")).hexdigest()
    else:
        # 旧加密模式（SHA1两次哈希）
        pwd_key = pwd + key
        pwd_hash = hashlib.sha1(pwd_key.encode("utf-8")).hexdigest()
        return hashlib.sha1((nonce + pwd_hash).encode("utf-8")).hexdigest()


# 移除不再需要的get_router_info函数
def get_router_info(ip):
    """获取路由器加密模式"""
    url = f"http://{ip}/cgi-bin/luci/api/xqsystem/init_info"
    try:
        response = requests.get(url, verify=False, timeout=5)
        data = response.json()
        return data.get("newEncryptMode", 0) != 0
    except Exception as e:
        print(f"获取路由器信息失败: {str(e)}")
        return False


def login_router(ip, password, key):
    nonce = create_nonce()
    # 强制使用新加密模式
    encrypt_mode = get_router_info(ip)

    # 生成加密密码
    encrypted_pwd = hash_password(password, nonce, key, encrypt_mode)

    # 构造请求参数
    url = f"http://{ip}/cgi-bin/luci/api/xqsystem/login"
    params = {
        "username": "admin",
        "password": encrypted_pwd,
        "logtype": "2",  # 新增必要参数
        "nonce": nonce

    }

    try:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url, data=params, headers=headers, verify=False, timeout=10)

        result = response.json()

        if result.get("code") == 0:
            return result.get("token")
        else:
            print(f"登录失败: {result}")
            return None

    except Exception as e:
        print(f"请求异常: {str(e)}")
        return None


if __name__ == "__main__":
    router_ip = "192.168.31.1"  # 路由器管理IP
    router_password = input("请输入路由器密码: ")
    router_key = "a2ffa5c9be07488bbb04a3a47d3c5f6a"  # 新机型似乎都需要,浏览器源码搜索"Encrypt"找到"key"对应值

    token = login_router(router_ip, router_password, router_key)
    if token:
        print(f"登录成功！Token: {token}")
