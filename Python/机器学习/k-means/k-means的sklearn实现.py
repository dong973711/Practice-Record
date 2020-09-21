import matplotlib.pyplot as plt
import sklearn.cluster as sc
import pandas as pd

# 获取数据
dataSet = pd.read_csv("data.csv", header=None, names=['X', 'Y'])
# print(type(dataSet))

# k-means聚类算法
model = sc.KMeans(n_clusters=3)
model.fit(dataSet)  # 完成聚类
result = model.predict(dataSet) # 数据集各个点在哪个类中
print(result)  # 输出每个样本的聚类标签
# 聚类中心，也就是质心
center_cores = model.cluster_centers_
print("质心：", center_cores)


# 画图
dataSet = dataSet.values  # 转换成数组形式，因为原型不能像下面这样操作
for i in range(len(dataSet)):
    if result[i] == 0:
        scatter1 = plt.scatter(dataSet[i][0], dataSet[i][1], marker='o', color='green', s=40, label='0类点')
    elif result[i] == 1:
        scatter2 = plt.scatter(dataSet[i][0], dataSet[i][1], marker='o', color='red', s=40, label='1类点')
    elif result[i] == 2:
        scatter3 = plt.scatter(dataSet[i][0], dataSet[i][1], marker='o', color='blue', s=40, label='2类点')
plt.rcParams['font.sans-serif'] =['SimHei']
plt.rcParams['axes.unicode_minus'] = False
for i in center_cores:
    scatter4 = plt.scatter(i[0],i[1], marker='x', color='black', s=40, label='质心')
plt.legend(handles=[scatter1, scatter2, scatter3, scatter4], labels=['0类点', '1类点', '2类点', '质心'], loc='best')
plt.show()
