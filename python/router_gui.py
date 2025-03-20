import os
import threading
import time
import tkinter as tk
from tkinter import ttk, messagebox

import api_client
import no_token_api
from login_router import login_router
from python.logger import RouterLogger


class RouterDashboard:
    def __init__(self, master, router_ip, token, password, key, precheck_data=None):
        self.master = master
        self.router_ip = router_ip
        self.token = token
        self.admin_pwd = password
        self.encrypt_key = key
        self.precheck_data = precheck_data  # 接收预检测数据

        master.title("小米路由器监控系统")
        master.geometry("800x800")

        # 新增顶部工具栏
        self.toolbar = ttk.Frame(master)
        self.toolbar.pack(side=tk.TOP, fill=tk.X, padx=20, pady=5)

        self.refresh_token_btn = ttk.Button(self.toolbar, text="刷新token", command=self.refresh_token)
        self.refresh_token_btn.pack(side=tk.LEFT, padx=5)
        RouterLogger.log_operation("GUI_OPERATION", "初始化主界面成功")

        # 新增Token显示文本框
        self.token_var = tk.StringVar(value=f"当前Token: {self.token}")
        self.token_entry = ttk.Entry(self.toolbar,
                                     textvariable=self.token_var,
                                     width=40,
                                     state='readonly',
                                     font=('Consolas', 10))
        self.token_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.rebot_btn = ttk.Button(self.toolbar, text="重启路由器", command=self.reboot)
        self.rebot_btn.pack(side=tk.LEFT, padx=5)

        # 状态信息面板
        self.info_frame = ttk.LabelFrame(master, text="路由器基本信息")
        self.info_frame.pack(pady=20, padx=20, fill=tk.X)

        self.init_info_labels = {
            'hardware': self.create_init_info_labels("硬件型号:", 0),
            'language': self.create_init_info_labels("语言:", 1),
            'romversion': self.create_init_info_labels("固件版本:", 2),
            'countrycode': self.create_init_info_labels("国家代码:", 3),
            'id': self.create_init_info_labels("设备序列号:", 4),
            'routername': self.create_init_info_labels("路由器名称:", 5),
            'display_name': self.create_init_info_labels("显示名称:", 6),
            'model': self.create_init_info_labels("设备型号:", 7),
            'routerId': self.create_init_info_labels("米家ID:", 8)
        }

        # 新增网络状态面板
        self.status_frame = ttk.LabelFrame(self.master, text="网络接口状态")
        self.status_frame.pack(pady=10, padx=20, fill=tk.X)
        # 添加WAN/LAN状态标签
        self.net_labels = {
            'wan_ip': self.create_status_label("WAN IPv4", 0),
            'wan': self.create_status_label("WAN 状态", 1),
            'wan_speed': self.create_status_label("WAN 速度", 2),
            'lan_ip': self.create_status_label("LAN IPv4", 3),
            'lan': self.create_status_label("LAN 状态", 4),
            'lan_speed': self.create_status_label("LAN 速度", 5)
        }

        # 新增系统状态面板
        # 修正：这里 master 应该替换为 self.master，因为在类的方法中，需要使用类的实例属性
        self.system_frame = ttk.LabelFrame(self.master, text="系统状态")
        self.system_frame.pack(pady=10, padx=20, fill=tk.X)

        # 系统状态标签布局
        self.sys_labels = {
            'mem': self.create_sys_label("内存使用", 0),
            'devices': self.create_sys_label("在线设备", 1),
            'total': self.create_sys_label("内存大小", 2),
            'hz': self.create_sys_label("CPU频率", 3),
            'type': self.create_sys_label("内存类型", 4)
        }

        # 新增设备列表面板
        self.device_frame = ttk.LabelFrame(master, text="连接设备列表")
        self.device_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # 创建Treeview表格
        self.device_tree = ttk.Treeview(self.device_frame,
                                        columns=('IPv4地址', 'MAC地址', '设备名称', '上传速度', '下载速度', '在线时长'),
                                        show='headings')

        # 配置列参数
        columns_config = {
            'IPv4地址': {'width': 150, 'anchor': tk.W},
            'MAC地址': {'width': 150, 'anchor': tk.W},
            '设备名称': {'width': 150},
            '上传速度': {'width': 100},
            '下载速度': {'width': 100},
            '在线时长': {'width': 100}
        }

        for col, config in columns_config.items():
            self.device_tree.heading(col, text=col)
            self.device_tree.column(col, **config)

        # 添加滚动条
        scrollbar = ttk.Scrollbar(self.device_frame, orient=tk.VERTICAL, command=self.device_tree.yview)
        self.device_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.device_tree.pack(fill=tk.BOTH, expand=True)

        if self.precheck_data:
            self._update_basic_info()
        else:
            # Bug修复: 将字符串转换为Exception对象
            RouterLogger.log_error("Invalid precheck_data format",
                                   exception=Exception("Expected dict got " + str(type(self.precheck_data))))

    def create_init_info_labels(self, text, row):
        """创建统一格式的状态标签"""
        lbl = ttk.Label(self.info_frame, text=f"{text}: 加载中...")
        lbl.grid(row=row, column=0, sticky=tk.W, padx=10, pady=5)
        return lbl

    def create_status_label(self, text, row):
        """创建统一格式的状态标签"""
        lbl = ttk.Label(self.status_frame, text=f"{text}: 加载中...")
        lbl.grid(row=row, column=0, sticky=tk.W, padx=10, pady=2)
        return lbl

    def create_sys_label(self, text, column):
        """创建系统状态标签"""
        lbl = ttk.Label(self.system_frame, text=f"{text}: 加载中...")
        lbl.grid(row=0, column=column, padx=10, pady=5, sticky=tk.W)
        return lbl

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

    def _update_basic_info(self):
        """更新基本信息面板的标签内容"""
        try:
            # self.init_info_labels['key'].config(text=f"{label}: {value}")
            for key, label in self.init_info_labels.items():
                label_text = label.cget("text").split(":")[0]
                value = getattr(self.precheck_data, key)
                self.init_info_labels[key].config(text=f"{label_text}: {value}")
            RouterLogger.log_operation("GUI_UPDATE", "基本信息面板更新完成")
        except Exception as e:
            RouterLogger.log_error("基本信息更新失败", e)
            # messagebox.showerror("更新错误", "基本信息加载失败，请检查数据源")


class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("路由器登录")
        master.geometry("400x250")

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

        self._schedule_ip_check()

    def _schedule_ip_check(self):
        if self.timer:
            self.master.after_cancel(self.timer)
        self.timer = self.master.after(500, self._check_ip_validity)

    def _check_ip_validity(self):
        ip = self.ip_entry.get()
        if not ip:
            return

        try:
            client = no_token_api.NoTokenAPI(self.master, ip)
            data = client.get_init_info()
            self.master.after(0, self._update_precheck_status, data)
            print(f"结束检查IP:{data}")
        except Exception as e:
            self.master.after(0, self.status_label.config, {
                'text': f'未发现设备,请检查设备是否连接,IP地址是否正确.',
                'foreground': 'orange'
            })
        # def check_task():
        #     try:
        #         client = no_token_api.NoTokenAPI(self.master, ip)
        #         data = client.get_init_info()
        #         self.master.after(0, self._update_precheck_status, data)
        #         print(f"结束检查IP:{data}")
        #     except Exception as e:
        #         self.master.after(0, self.status_label.config, {
        #             'text': f'未发现设备,请检查设备是否连接,IP地址是否正确.',
        #             'foreground': 'orange'
        #         })
        #
        # threading.Thread(target=check_task, daemon=True).start()

    def _update_precheck_status(self, data):
        self.status_label.config(text="已发现路由器" + data.routername, foreground="green")
        self.precheck_data = data

    def do_login(self):
        ip = self.ip_entry.get()
        pwd = self.pwd_entry.get()
        key = self.key_entry.get()

        if not all([ip, key]) or not pwd:  # 强化密码非空检查
            messagebox.showerror("错误", "所有字段必须填写且密码不能为空")
            return

        token = login_router(ip, pwd, key)
        if token:
            RouterLogger.log_operation("登录成功", f"用户成功登录:{token}")
            self.master.destroy()
            root = tk.Tk()
            # 新增传递password和key参数
            RouterDashboard(root, ip, token, pwd, key, self.precheck_data)
            root.mainloop()
        else:
            messagebox.showerror("错误", "登录失败，请检查凭证")
            RouterLogger.log_error("登录失败", token)


if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()
