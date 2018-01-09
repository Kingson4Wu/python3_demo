import pandas as pd
import matplotlib.pyplot as plt

'''
阅读数分布比例
'''

name = ['日期', '时间', '标题', '作者', '摘要', '创作类型', '是否头条号', '阅读数', '点赞数', '评论数', '地址']
df = pd.read_excel('weixin.xlsx', encoding='utf-8', header=0, names=name)
data = df[['阅读数']]
a = data.sort_values(by=['阅读数'], ascending=False)
one = a[a['阅读数'] >= 70000].size
two = a[(a['阅读数'] >= 30000) & (a['阅读数'] < 70000)].size
three = a[(a['阅读数'] >= 10000) & (a['阅读数'] < 30000)].size
four = a[(a['阅读数'] >= 1000) & (a['阅读数'] < 10000)].size
five = a[(a['阅读数'] < 1000)].size
explode = [0.3, 0, 0, 0, 0]
fras = [one, two, three, four, five]
plt.figure(figsize=(15, 5))
plt.axes(aspect=1)
plt.title('阅读数分布比例', fontsize=18)
plt.pie(x=fras, autopct='%.2f%%', explode=explode, shadow=True,
        labels=['大于70,000', '30,000~70,000', '10,000~30,000', '1000~10,000', '小于1,000'])
plt.show()
