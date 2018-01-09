# coding=utf-8
# !/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager, FontProperties

'''
https://mp.weixin.qq.com/s/RzJdAioereq7D0og8iS4XA
数据分析
'''
def getChineseFont():
    return FontProperties(fname='simhei.ttf')


name = ['日期', '时间', '标题', '作者', '摘要', '创作类型', '是否头条号', '阅读数', '点赞数', '评论数', '地址']
df = pd.read_excel('weixin.xlsx', encoding='utf-8', header=0, names=name)
df['文章数'] = pd.to_datetime(df['日期']).dt.month
date = pd.DataFrame(df['文章数'].value_counts())
plt.figure(figsize=(15, 5))
plt.title('CSDN公众号文章发布情况', fontproperties=getChineseFont())
plt.xlabel('月份', fontproperties=getChineseFont())
plt.ylabel('文章数', fontproperties=getChineseFont())
plt.xticks((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), (
    '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10',
    '2017-11',
    '2017-12'))
plt.plot(date.sort_index(), color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=8)
plt.show()
