
import pandas as pd
import matplotlib.pyplot as plt

'''
阅读数 TOP10 的文章
'''

name = ['日期', '时间', '标题', '作者', '摘要', '创作类型', '是否头条号', '阅读数', '点赞数', '评论数', '地址']
df = pd.read_excel('weixin.xlsx', encoding='utf-8', header=0, names=name, )
df_read = df[['标题', '阅读数']]
data_read = df.sort_values(by=['阅读数'], ascending=False)
data_read.index = data_read['标题']
var = data_read['阅读数'][:10]
plt.figure(figsize=(15, 6))
plt.title('阅读数 TOP10 的文章', fontsize=18)
plt.xlabel('数量', fontsize=18)
plt.ylabel('标题', fontsize=18)
var.plot(kind='barh', stacked=True, alpha=0.5, color=['red'])
plt.show()
