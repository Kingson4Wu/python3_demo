import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

'''
https://mp.weixin.qq.com/s/RzJdAioereq7D0og8iS4XA
数据分析
'''
from matplotlib.font_manager import _rebuild

_rebuild()
# 防止中文乱码问题
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False


def getChineseFont():
    return FontProperties(fname='simhei.ttf')


name = ['日期', '时间', '标题', '作者', '摘要', '创作类型', '是否头条号', '阅读数', '点赞数', '评论数', '地址']
df = pd.read_excel('weixin.xlsx', encoding='utf-8', header=0, names=name)
data = pd.DataFrame(df['创作类型'].value_counts())
explode = [0, 0, 0, 0, 0]
plt.figure(figsize=(15, 6))
plt.axes(aspect=1)
plt.title('文章创作情况', fontsize=18, fontproperties=getChineseFont())
plt.pie(x=data, autopct='%.2f%%', explode=explode, shadow=True, labels=['原创', '未标记作者', '创作或转发', '其它', '未知'])
plt.show()
