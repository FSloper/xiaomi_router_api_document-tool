import tkinter as tk
from tkinter import ttk
import time
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class DeviceGraphWindow(tk.Toplevel):
    def __init__(self, master, device_tree):
        super().__init__(master)
        self.title("设备流量监控")
        self.geometry("800x600")
        self.device_tree = device_tree
        self.data_history = {}

        # 创建图表
        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # 初始化定时器
        self.update_interval = 5000  # 5秒
        self.update_chart()

    def get_current_data(self):
        data = {
            'timestamp': time.time(),
            'devices': []
        }
        for child in self.device_tree.get_children():
            values = self.device_tree.item(child)['values']
            device_name = values[2]
            upload = float(values[4].split()[0])  # 提取数值部分
            download = float(values[5].split()[0])
            data['devices'].append({
                'name': device_name,
                'upload': upload,
                'download': download
            })
        return data

    def update_chart(self):
        current_data = self.get_current_data()
        timestamp = current_data['timestamp']

        # 更新数据历史
        for device in current_data['devices']:
            if device['name'] not in self.data_history:
                self.data_history[device['name']] = {
                    'upload': [],
                    'download': [],
                    'timestamps': []
                }
            
            hist = self.data_history[device['name']]
            hist['upload'].append(device['upload'])
            hist['download'].append(device['download'])
            hist['timestamps'].append(timestamp)
            
            # 保持最近10个数据点
            if len(hist['upload']) > 10:
                hist['upload'] = hist['upload'][-10:]
                hist['download'] = hist['download'][-10:]
                hist['timestamps'] = hist['timestamps'][-10:]

        # 清空图表重新绘制
        self.ax.clear()
        
        # 为每个设备绘制两条线（上传/下载）
        for device_name, data in self.data_history.items():
            if len(data['timestamps']) > 1:
                # 上传速度用实线
                self.ax.plot(
                    data['timestamps'],
                    data['upload'],
                    label=f'{device_name} 上传',
                    linestyle='-'
                )
                # 下载速度用虚线
                self.ax.plot(
                    data['timestamps'],
                    data['download'], 
                    label=f'{device_name} 下载',
                    linestyle='--'
                )

        self.ax.set_xlabel('时间')
        self.ax.set_ylabel('速度 (MB/s)')
        self.ax.legend(loc='upper left')
        self.ax.grid(True)
        self.canvas.draw()

        # 设置下一次更新
        self.after(self.update_interval, self.update_chart)

    def destroy(self):
        # 停止定时器
        if hasattr(self, 'after_id'):
            self.after_cancel(self.after_id)
        super().destroy()