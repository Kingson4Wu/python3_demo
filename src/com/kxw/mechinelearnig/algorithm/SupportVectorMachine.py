
# coding:utf-8

'''

https://mp.weixin.qq.com/s/x862NJ3iHS5pGVXhd-uf3w

支持向量机
支持向量机（SVM）是从线性可分情况下的最优分类面发展而来。最优分类面就是要求分类线不但能将两类正确分开 (训练错误率为 0), 且使分类间隔最大。

SVM 考虑寻找一个满足分类要求的超平面 , 并且使训练集中的点距离分类面尽可能的远 , 也就是寻找一个分类面使它两侧的空白区域 (margin) 最大。

这两类样本中离分类面最近的点且平行于最优分类面的超平面上 H1,H2 的训练样本就叫做支持向量。


例：使用 sklearn 库实现 svm 算法， 俗称调库，实际上调库是一个很简单的过程，初级阶段甚至都不需要知道原理。

'''


from sklearn import svm
X = [[2,0], [1,1], [2,3]]
y = [0,0,1]
clf = svm.SVC(kernel = 'linear')
clf.fit(X,y)  #ͨ通过 .fit 函数已经可以算出支持向量机的所有参数并保存在 clf 中

print clf

# get support vectors
print clf.support_vectors_

#get index of support vectors
print clf.support_

#get number of support vectors for each class
print clf.n_support_

#predict data , 参数是二维数组
print clf.predict([[2, 0], [10,10]])