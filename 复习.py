-*- coding:utf-8 -*-

import psutil
 # Day1 写一个脚本：输入服务器 IP，打印“正在连接…”
ip = (input("请输入一个IP："))
print(f'正在连接{ip}')


 # Day2 判断磁盘使用率：>80% 打印“警告”，否则“正常”
Threshold = 80

disk_info = psutil.disk_usage('/')

if disk_info.percent > Threshold:
    print(f"硬盘利用率为{disk_info.percent}%,超过{Threshold}%")
else:
    print(f"硬盘利用率为{disk_info.percent}%,符合{Threshold}%")

 # Day3 遍历一个 IP 列表，打印每个 IP 的 ping 命令
ip_list = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5']

for ip in ip_list:
    print(f'ping {ip}')


ip_init = 0
while ip_init <  len(ip_list):
    print(f' [{ip_init + 1 }] ping {ip_list[ip_init]}')
    ip_init = ip_init + 1


# Day4  存 3 台服务器信息（IP、用途），打印出来
server_list = {
    '192.168.1.1':'应用IP',
    '192.168.1.2':'业务IP',
    '192.168.1.3':'心跳IP'
}

for key,value in server_list.items():
    print(key, value)

server1_list = []


# Day5 写一个函数 check_disk(path)，返回磁盘使用率
def check_disk():
    disk_usage = psutil.disk_usage('/')
    return disk_usage.percent
 disk_usage = (check_disk())
print(f"磁盘利用率为：{disk_usage}%")
GPT修改版
def check_disk(path):
    disk_usage = psutil.disk_usage(path)
    return disk_usage.percent
 usage = check_disk('/')
print(f"磁盘利用率为：{usage}%")

#Day6 读取一个文件，逐行打印
with open(r'D:\Users\Administrator\Desktop\问题.txt',encoding='UTF-8') as f:
    readlines = f.readlines()
    for line in readlines:
        print(line.strip())
 #Day 7
try:
    with open(r'D:\Users\Administrator\Desktop\问题1123.txt',encoding='UTF-8') as f:
        content = f.readlines()
        print(content)
except FileNotFoundError:
    print('没找到这个文件')

