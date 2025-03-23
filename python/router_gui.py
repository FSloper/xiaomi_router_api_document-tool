import os
import threading
import time
import tkinter as tk
from tkinter import ttk, messagebox

import api_client
import api_invoke
from logger import RouterLogger
from login_router import login_router


def create_label(frame, text, row=0, column=0, padx=10, pady=5, sticky=tk.W):
    """通用标签创建方法"""
    lbl = ttk.Label(frame, text=f"{text}: 加载中...")
    lbl.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
    return lbl


def put_label_in_frame(definitions, label, frame, column_num=1):
    for idx, (key, text) in enumerate(definitions):
        row = idx // column_num  # 每行显示2列
        column = idx % column_num
        label[key] = create_label(
            frame,
            text,
            row=row,
            column=column
        )


class RouterDashboard:
    def __init__(self, master, router_ip, token, password, key, precheck_data=None):
        self.master = master
        self.router_ip = router_ip
        self.token = token
        self.admin_pwd = password
        self.encrypt_key = key
        self.precheck_data = precheck_data  # 接收预检测数据

        master.title("小米路由器监控系统")
        master.geometry("1000x800")

        # 新增顶部工具栏
        self.toolbar = ttk.Frame(master)
        self.toolbar.pack(side=tk.TOP, fill=tk.X, padx=20, pady=5)

        self.refresh_token_btn = ttk.Button(self.toolbar, text="刷新token", command=self.refresh_token)
        self.refresh_token_btn.pack(side=tk.LEFT, padx=5)
        RouterLogger.log_operation("GUI_OPERATION", "初始化主界面成功")

        # 新增Token显示文本框
        self.token_var = tk.StringVar(value=f"数据可能异常")
        self.token_entry = ttk.Entry(self.toolbar,
                                     textvariable=self.token_var,
                                     width=40,
                                     state='readonly',
                                     font=('Consolas', 10))
        self.token_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.token_var.set(f"当前Token: {self.token}")

        self.rebot_btn = ttk.Button(self.toolbar, text="重启路由器", command=self.reboot)
        self.rebot_btn.pack(side=tk.LEFT, padx=5)

        # 状态信息面板
        self.info_frame = ttk.LabelFrame(master, text="路由器基本信息")
        self.info_frame.pack(pady=20, padx=20, fill=tk.X)

        init_info_definitions = [
            ('hardware', "硬件型号"),
            ('language', "语言"),
            ('romversion', "固件版本"),
            ('countrycode', "国家代码"),
            ('id', "设备序列号"),
            ('routername', "路由器名称"),
            ('display_name', "显示名称"),
            ('model', "设备型号"),
            ('routerId', "米家ID"),
            ('total', "内存大小"),
            ('hz_ddr', "内存频率"),
            ('type', "内存类型"),
            ('hz_cpu', "CPU频率"),
            ('core', "核心数"),
            ('temperature', "温度"),
            ('mac', "MAC地址")
        ]
        self.init_info_labels = {
        }
        put_label_in_frame(init_info_definitions, self.init_info_labels, self.info_frame, 3)

        # 新增网络状态面板
        self.status_frame = ttk.LabelFrame(self.master, text="网络接口状态")
        self.status_frame.pack(pady=10, padx=20, fill=tk.X)
        net_definitions = [
            ('wan_ip', "上级分配IPv4"),
            ('wanType', "上级上网方式"),
            ('lan_ip', "下级分配IPv4"),
            ('dnsAddrs', "DNS 地址1"),
            ('dnsAddrs1', "DNS 地址2")
        ]
        self.net_labels = {
        }
        put_label_in_frame(net_definitions, self.net_labels, self.status_frame, 2)

        self.system_frame = ttk.LabelFrame(self.master, text="动态数据")
        self.system_frame.pack(pady=10, padx=20, fill=tk.X)

        sys_definitions = [
            ('upTime', "运行时间"),
            ('usage', "内存使用"),
            ('online', "在线设备"),
            ('download', "下载速度"),
            ('upspeed', "上传速度")
        ]
        self.sys_labels = {
        }
        put_label_in_frame(sys_definitions, self.sys_labels, self.system_frame, 2)

        # 新增设备列表面板
        self.device_frame = ttk.LabelFrame(master, text="连接设备列表")
        self.device_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # 创建Treeview表格
        self.device_tree = ttk.Treeview(self.device_frame,
                                        columns=('连接方式', 'MAC地址', '设备名称', 'IPv4地址', '上传速度', '下载速度',
                                                 '在线时长'),
                                        show='headings')

        # 配置列参数
        columns_config = {
            '连接方式': {'width': 100},
            'MAC地址': {'width': 150, 'anchor': tk.W},
            '设备名称': {'width': 150},
            'IPv4地址': {'width': 150, 'anchor': tk.W},
            '上传速度': {'width': 100},
            '下载速度': {'width': 100},
            '在线时长': {'width': 100, 'anchor': tk.W}
        }

        for col, config in columns_config.items():
            self.device_tree.heading(col, text=col)
            self.device_tree.column(col, **config)

        # 添加滚动条
        scrollbar = ttk.Scrollbar(self.device_frame, orient=tk.VERTICAL, command=self.device_tree.yview)
        self.device_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.device_tree.pack(fill=tk.BOTH, expand=True)

        self.up_basic_data()
        self.up_net_data()

    def up_basic_data(self):
        def update_data():
            if self.precheck_data:
                self._update_basic_data(self.init_info_labels, self.precheck_data)
                data = api_invoke.NeedTokenAPI(self.master, self.router_ip, self.token).get_sys_status()
                self._update_basic_data(self.init_info_labels, data)
                informationdata = api_invoke.NeedTokenAPI(self.master, self.router_ip, self.token).get_information()
                self._update_basic_data(self.net_labels, informationdata)
            else:
                # Bug修复: 将字符串转换为Exception对象
                RouterLogger.log_error("Invalid precheck_data format",
                                       exception=Exception("Expected dict got " + str(type(self.precheck_data))))

        threading.Thread(target=update_data, daemon=True).start()

    def up_net_data(self):
        def update_data():
            data = api_invoke.NeedTokenAPI(self.master, self.router_ip, self.token).get_sys_status()
            # TODO 转换问题
            self._update_basic_data(self.sys_labels, data)
            devices = api_invoke.NeedTokenAPI(self.master, self.router_ip, self.token).get_device_list()
            self.update_device_list(devices)
            threading.Timer(5, update_data).start()

        threading.Thread(target=update_data, daemon=True).start()

    def update_device_list(self, devices):
        """更新设备列表数据"""
        # 清空旧数据
        for item in self.device_tree.get_children():
            self.device_tree.delete(item)

        # 填充新数据
        for dev in devices:
            self.device_tree.insert('', tk.END, values=(
                dev['type'],
                dev['mac'],
                dev['name'],
                dev['ip'],
                f"{self.format_speed(dev['upspeed'])}",
                f"{self.format_speed(dev['downspeed'])}",
                self.format_online_time(dev['online'])
            ))

    def format_speed(self, speed):
        """格式化速度显示 (B/s -> MB/s)"""
        # TODO 转换问题
        speed = float(speed)
        if speed >= 100:
            return f"{speed / 102400:.2f} MB/s"
        else:
            return f"{speed / 1024:.2f} KB/s"

    def format_online_time(self, seconds):
        """格式化在线时长"""
        hours = int(float(seconds) // 3600)
        minutes = int((float(seconds) % 3600) // 60)
        return f"{hours}时{minutes:02}分"

    def refresh_token(self):
        """执行完整的token刷新流程"""
        RouterLogger.log_operation("GUI_OPERATION", "用户点击刷新设备列表")
        try:
            new_token = login_router(self.router_ip, self.admin_pwd, self.encrypt_key)

            if new_token and new_token != self.token:
                self.token = new_token
                self.token_var.set(f"当前Token: {self.token}")  # 更新文本框内容
                messagebox.showinfo("刷新成功", "Token已更新，新token值:\n" + self.token)
                RouterLogger.log_operation("New token:", self.token)
            elif new_token:
                messagebox.showinfo("提示", "Token未变化，仍为当前有效token")
                RouterLogger.log_operation("Token未变化", "Token未变化，仍为当前有效token")
            else:
                raise Exception("API返回空token")

        except Exception as e:
            RouterLogger.log_error("刷新设备列表失败", e)
            messagebox.showerror("刷新失败", f"Token刷新失败:\n{str(e)}")

    def reboot(self):
        if not messagebox.askyesno("确认重启", "确定要重启路由器吗？该操作需要约3分钟完成"):
            return

        self.rebot_btn.config(state=tk.DISABLED, style='Disabled.TButton')
        RouterLogger.log_operation("GUI_OPERATION", "用户点击重启按钮，按钮已禁用")

        def reboot_task():
            try:
                client = api_client.APIClient(
                    self.router_ip,
                    self.token,
                    self.admin_pwd,
                    self.encrypt_key
                )
                response = client.reboot_router()

                if response.get('code') == 0:
                    self.master.after(0,
                                      lambda: messagebox.showinfo("重启成功", "路由器正在重启，请等待3分钟后重新连接"))
                else:
                    raise Exception(f"API错误: {response.get('msg', '未知错误')}")

            except Exception as e:
                self.master.after(0, lambda: messagebox.showerror("重启失败", str(e)))
            finally:
                self.master.after(0, lambda: self.rebot_btn.config(state=tk.NORMAL))

        threading.Thread(target=reboot_task, daemon=True).start()
        self._start_ip_monitoring()

    def _start_ip_monitoring(self):
        """启动IP可达性监控线程"""

        def monitor_task():
            RouterLogger.log_operation("IP_MONITOR", "开始持续检测路由器IP状态")
            while True:
                try:
                    response = os.system(f"ping -n 1 -w 1000 {self.router_ip} >nul")
                    if response == 0:
                        RouterLogger.log_operation("IP_MONITOR", "检测到路由器已恢复在线")
                        self.master.after(0, self._handle_router_recovered)
                        break
                    time.sleep(1)
                except Exception as e:
                    RouterLogger.log_error("IP监控异常", e)

        threading.Thread(target=monitor_task, daemon=True).start()

    def _handle_router_recovered(self):
        """处理路由器恢复后的token刷新"""
        try:
            client = api_client.APIClient(
                self.router_ip,
                self.token,
                self.admin_pwd,
                self.encrypt_key
            )
            new_token = client.refresh_token()
            if new_token:
                self.token = new_token
                self.token_var.set(f"当前Token: {self.token}")
                messagebox.showinfo("系统恢复", "路由器已重启完成，新token已自动更新")
                self.rebot_btn.config(state=tk.NORMAL, style='TButton')
                RouterLogger.log_operation("GUI_OPERATION", "路由器恢复完成，按钮状态已重置")
        except Exception as e:
            messagebox.showerror("刷新失败", f"自动获取token失败:\n{str(e)}")

    def _update_basic_data(self, label, data):
        try:
            for key, label in label.items():
                value = getattr(data, key, None)
                if value is None:
                    continue
                if value == '1':
                    value = "是"
                elif value == '0':
                    value = "否"
                label_text = label.cget("text").split(":")[0]
                label.config(text=f"{label_text}: {value}")
            RouterLogger.log_operation("GUI_UPDATE", "基本信息面板更新完成")
        except Exception as e:
            RouterLogger.log_error("基本信息更新失败", e)
            print(e)


class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("路由器登录")
        master.geometry("400x250")
        self.precheck_data = None

        ttk.Label(master, text="路由器IP:").grid(row=0, padx=10, pady=5, sticky=tk.W)
        self.ip_entry = ttk.Entry(master)
        self.ip_entry.grid(row=0, column=1, padx=10, pady=5)
        self.ip_entry.insert(0, "192.168.31.1")
        # self.ip_entry.bind("<KeyRelease>", self._schedule_ip_check)

        ttk.Label(master, text="管理员密码:").grid(row=1, padx=10, pady=5, sticky=tk.W)
        self.pwd_entry = ttk.Entry(master, show="*")
        self.pwd_entry.grid(row=1, column=1, padx=10, pady=5)
        self.pwd_entry.insert(0, "123w45678")

        ttk.Label(master, text="加密密钥:").grid(row=2, padx=10, pady=5, sticky=tk.W)
        self.key_entry = ttk.Entry(master)
        self.key_entry.grid(row=2, column=1, padx=10, pady=5)
        self.key_entry.insert(0, "a2ffa5c9be07488bbb04a3a47d3c5f6a")

        self.login_btn = ttk.Button(master, text="登录", command=self.do_login)
        self.login_btn.grid(row=3, columnspan=2, pady=20)

        # 添加状态提示标签
        self.status_label = ttk.Label(master, text="", foreground="gray", wraplength=380)
        self.status_label.grid(row=4, columnspan=2, sticky=tk.EW, padx=10)

        # 初始化定时器
        self.timer = None

        self._check_ip_validity()

    def _schedule_ip_check(self):
        if self.timer:
            self.master.after_cancel(self.timer)
        self.timer = self.master.after(0, self._check_ip_validity)

    def _check_ip_validity(self):
        ip = self.ip_entry.get()
        if not ip:
            return

        def check_task():
            try:
                data = api_invoke.NoTokenAPI(self.master, ip).get_init_info()
                self.master.after(0, self.status_label.config, {
                    'text': f'已发现路由器 {data.routername}',
                    'foreground': 'green'
                })
                self.precheck_data = data
            except Exception as e:
                self.master.after(0, self.status_label.config, {
                    'text': f'未发现设备,请检查设备是否连接,IP地址是否正确.',
                    'foreground': 'orange'
                })

        threading.Thread(target=check_task, daemon=True).start()

    def do_login(self):
        ip = self.ip_entry.get()
        pwd = self.pwd_entry.get()
        key = self.key_entry.get()

        if not all([ip, key]) or not pwd:  # 强化密码非空检查
            messagebox.showerror("错误", "所有字段必须填写且密码不能为空")
            return

        token = login_router(ip, pwd, key)
        if token:
            self.master.destroy()
            RouterLogger.log_operation("登录成功", f"用户成功登录:{token}")
            root = tk.Tk()
            RouterDashboard(root, ip, token, pwd, key, self.precheck_data)
            root.mainloop()
        else:
            messagebox.showerror("错误", "登录失败，请检查凭证")
            RouterLogger.log_error("登录失败", token)


if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()
