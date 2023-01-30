import csv

'''
https://mp.weixin.qq.com/s/x862NJ3iHS5pGVXhd-uf3w

决策树
判定树是一个类似于流程图的树结构：其中，每个内部结点表示在一个属性上的测试，每个分支代表一个属性输出，而每个树叶结点代表类或类分布。树的最顶层是根结点。

例：现有一个数据集，表示一些的人的年龄、收入、是否是学生、信用、是否会买电脑。年龄有年轻，中年，老年三种；收入有高中低；信用有一般和很好。数据及保存在 AllElectronics.csv 中。

现在在有一个新的人（数据），要判断这个人是否会买电脑。

'''

allElectronicsData = open(r'D:\deeplearning\AllElectronics.csv', 'rb')
reader = csv.reader(allElectronicsData)
headers = reader.next()

print(headers)
featureList = []
labelList = []  # 最后一列

for row in reader:
    # print(row)
    labelList.append(row[len(row) - 1])  # 在元祖末尾添加元素
    rowDict = {}
    for i in range(1, len(row) - 1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)
print(featureList)
print(labelList)

vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print("dummyX:" + str(dummyX))
print(vec.get_feature_names())

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY:" + str(dummyY))

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
print("clf: " + str(clf))

with open("allElectronicInformationGainDri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)  # 在当前工作目录生成  .dot 文件

oneRowX = dummyX[0, :]
print("oneRowx: " + str(oneRowX))

newRowX = oneRowX

newRowX[0] = 1
newRowX[2] = 0
print("newRowX: " + str(newRowX))

predictedY = clf.predict(newRowX)
print("predictedY:" + str(predictedY))
