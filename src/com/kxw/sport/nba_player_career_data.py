# -- coding: utf-8 --

# ————————————————
# 版权声明：本文为CSDN博主「AlchemyLee」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_44776064/article/details/105753326

import requests
from lxml import html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

etree = html.etree
url='https://nba.hupu.com/players/lebronjames-650.html'
data=requests.get(url).text
s=etree.HTML(data)


d=[[]for j in range(23)]
for j in range(23):
  for i in range (19):
    a=s.xpath('//*[@id="in_box"]/div/div[1]/table[2]/tbody/tr['+str(j)+']/td['+str(i)+']/text()')
    b=str(a)
    c=b[2:-2]
    d[j].append(c)

data1 = pd.DataFrame(d)
data1.to_csv('james_season.csv')

#plt.rcParams['font.sans-serif'] = ['KaiTi']  # 显示中文
#labels = np.array([u'时间', u'命中率', u'篮板',u'助攻',u'失误',u'得分']) # 标签
#dataLenth = 6  # 数据维度
#data_radar = np.array([james[0],james[1],james[2],james[3],james[4],james[5]]) # 数据
#angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)  # 分割圆周长
#data_radar = np.concatenate((data_radar, [data_radar[0]]))  # 闭合
#angles = np.concatenate((angles, [angles[0]]))  # 闭合
#plt.polar(angles, data_radar, 'bo-', linewidth=1)  # 做极坐标系
#plt.thetagrids(angles * 180/np.pi, labels)  # 做标签
#plt.fill(angles, data_radar, facecolor='magenta', alpha=0.25)# 填充  c  maroon
#plt.title(u'james生涯场均数据')
#plt.show()

