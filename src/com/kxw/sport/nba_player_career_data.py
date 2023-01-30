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


d=[[]for j in range(20)]
for j in range(20):
  for i in range (19):
    a=s.xpath('//*[@id="in_box"]/div/div[1]/table[2]/tbody/tr['+str(j)+']/td['+str(i)+']/text()')
    b=str(a)
    c=b[2:-2]
    d[j].append(c)

data1 = pd.DataFrame(d)
data1.to_csv('output.csv')
