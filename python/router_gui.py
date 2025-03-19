import tkinter as tk
from tkinter import ttk, messagebox

from login_router import login_router

class RouterDashboard:
    def __init__(self, master, router_ip, token):
        self.master = master
        self.router_ip = router_ip
        self.token = token
        print(self.token)

        master.title("小米路由器监控系统")
        master.geometry("800x800")

        # 状态信息面板
        self.info_frame = ttk.LabelFrame(master, text="路由器基本信息")
        self.info_frame.pack(pady=20, padx=20, fill=tk.X)

        # 初始化信息展示标签（使用enumerate优化布局）
        self.labels = {}
        fields = [
            ("hardware", "硬件型号"),
            ("romversion", "固件版本"),
            ("model", "设备型号"),
            ("countrycode", "国家代码"),
            ("routername", "路由器名称"),
            ("id", "设备序列号"),
            ("display_name", "显示名称"),
            ("mac", "MAC地址")
        ]

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

        for row_idx in range((len(fields) + 1) // 2):
            for col_idx in range(2):
                if (index := row_idx * 2 + col_idx) >= len(fields):
                    break
                key, text = fields[index]
                lbl = ttk.Label(self.info_frame, text=f"{text}: 加载中...")
                lbl.grid(row=row_idx, column=col_idx, sticky=tk.W, padx=10, pady=5)
                self.labels[key] = lbl
        # 新增设备列表面板
        self.device_frame = ttk.LabelFrame(master, text="连接设备列表")
        self.device_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # 创建Treeview表格
        self.device_tree = ttk.Treeview(self.device_frame,
                                        columns=('MAC地址', '设备名称', '上传速度', '下载速度', '在线时长'),
                                        show='headings')

        # 配置列参数
        columns_config = {
            'MAC地址': {'width': 150, 'anchor': tk.W},
            '设备名称': {'width': 150},
            '上传速度': {'width': 100},
            '下载速度': {'width': 100},
            '在线时长': {'width': 90}
        }

        for col, config in columns_config.items():
            self.device_tree.heading(col, text=col)
            self.device_tree.column(col, **config)

        # 添加滚动条
        scrollbar = ttk.Scrollbar(self.device_frame, orient=tk.VERTICAL, command=self.device_tree.yview)
        self.device_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.device_tree.pack(fill=tk.BOTH, expand=True)

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


class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("路由器登录")
        master.geometry("400x250")

        ttk.Label(master, text="路由器IP:").grid(row=0, padx=10, pady=5, sticky=tk.W)
        self.ip_entry = ttk.Entry(master)
        self.ip_entry.grid(row=0, column=1, padx=10, pady=5)
        self.ip_entry.insert(0, "192.168.31.1")

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

    def do_login(self):
        ip = self.ip_entry.get()
        pwd = self.pwd_entry.get()
        key = self.key_entry.get()

        if not all([ip, pwd, key]):
            messagebox.showerror("错误", "所有字段必须填写")
            return

        token = login_router(ip, pwd, key)
        if token:
            self.master.destroy()
            root = tk.Tk()
            RouterDashboard(root, ip, token)
            root.mainloop()
        else:
            messagebox.showerror("错误", "登录失败，请检查凭证")


if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()
