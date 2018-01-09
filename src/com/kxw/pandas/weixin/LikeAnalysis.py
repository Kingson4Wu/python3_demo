import pandas as pd
import matplotlib.pyplot as plt

'''
点赞数分析
'''
name = ['日期', '时间', '标题', '作者', '摘要', '创作类型', '是否头条号', '阅读数', '点赞数', '评论数', '地址']
df = pd.read_excel('weixin.xlsx', encoding='utf-8', header=1, names=name, )
data = df[['点赞数']]
a = data.sort_values(by=['点赞数'], ascending=False)
one = a[a['点赞数'] >= 200].size
two = a[(a['点赞数'] >= 50) & (a['点赞数'] < 200)].size
three = a[(a['点赞数'] < 50)].size
explode = [0.3, 0, 0]
fras = [one, two, three]
plt.figure(figsize=(15, 5))
plt.axes(aspect=1)
plt.title('点赞数分布比例', fontsize=18)
plt.pie(x=fras, autopct='%.2f%%', explode=explode, shadow=True, labels=['大于200', '50~100', '小于50'])
plt.show()
