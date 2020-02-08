# -- coding: utf-8 --
from scapy.all import *
# 数据包应用层数据部分
from scapy.layers.inet import IP, TCP

# https://blog.csdn.net/singleyellow/article/details/79737473
data = 'wangpeng'
# 发送端IP地址10.0.3.83不是本机ip地址   目的端IP地址不详      传输层的TCP并未指明数据包类型：syn fin ack 窗口大小 数据包如果分片，要指明序号
pkt = IP(src='10.0.3.83', dst='10.0.3.88') / TCP(sport=12345, dport=5555) / data
# 间隔一秒发送一次   总共发送5次   发送网卡口：enp1s0
send(pkt, inter=1, count=5, iface="enp1s0")

# 我们可以拿 scapy 做什么:<http://sinhub.cn/2018/06/what-can-we-do-with-scapy/>
# 嗅探实例
packets = scapy.sniff(filter="tcp and port 80 and target www.acfun.cn", count=3)
