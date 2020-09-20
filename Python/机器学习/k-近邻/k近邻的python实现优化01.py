import csv
import numpy as np
import matplotlib.pyplot as plt


# 每个数据包括三列，[x,y,label] .x,y分别为两个属性，label为该数据的类别
def createDataSet():
    dataset = []
    for line in open("data.csv"):
        x, y, label = line.split(",")
        dataset.append([int(x), int(y), int(label)])
    return dataset


# 计算各点到预测点的距离
def calcDis(dataSet, socuse, k):
    calcList = []
    dataSet = np.array(dataSet)
    dataSize = dataSet.shape[0]
    dataSet1 = np.delete(dataSet, 2, axis=1)
    """
       将socuse在横向重复dataSetSize次，纵向重复1次
       例如socuse=([1,2])--->([[1,2],[1,2],[1,2],[1,2]])便于后面计算距离
    """
    diff = np.tile(socuse, (dataSize, 1)) - dataSet1
    """
       计算距离:欧式距离, 特征相减后乘方,然后再开方
    """
    sqdifMax = diff ** 2
    seqDistances = sqdifMax.sum(axis=1)
    calcList = seqDistances ** 0.5
    # print(calcList)

    # for i in range(len(dataSet)):
    #     calcList.append(
    #         (((socuse[0] - dataSet[i][0]) ** 2 + (socuse[1] - dataSet[i][1]) ** 2) ** 0.5))
    # # print("各点与质心的距离：",calcList)
    # calcList = np.array(calcList)
    dis_sort_index = np.argsort(calcList)  # 排序并且得到的是排序后的下标
    # dis_sort_index_near = dis_sort_index[0:k]  # 取得前k个下标
    for i in range(k):  # 查看前k个到底是哪一类
        print(dataSet[dis_sort_index[i]])
    # print(dis_sort_index_near)
    # labels = []
    counts = [0, 0, 0]  # 记录前k个数据中各标签出现的个数
    for i in range(k):
        # labels.append(dataSet[dis_sort_index_near[i]])
        # print(dataSet[dis_sort_index_near[i]][2])
        # counts[dataSet[dis_sort_index_near[i]][2]] += 1
        counts[dataSet[dis_sort_index[i]][2]] += 1
    max_label = 0
    # max_value = 0
    # for i in range(5):
    #     if counts[i] > max_value:
    #         max_value = counts[i]
    #         max_label = i
    # print(counts)
    counts_sort = np.argsort(counts)
    # print(counts_sort)
    max_label = counts_sort[2]
    return max_label, dis_sort_index[0:k]


if __name__ == '__main__':
    dataSet = createDataSet()
    for data in dataSet:
        plt.scatter(data[0], data[1], marker='o', color='green', s=40, label='原始点')
    a = [13, 17]
    plt.scatter(a[0], a[1], marker='o', color='red', s=40, label='预测点')
    k = 5
    b, near_point = calcDis(dataSet, a, k)
    print(a, "被预测为的类别是:", b)
    '''
    增加预测点与最近点的连线
    '''
    x = []
    y = []
    for i in range(k):
        x.append(a[0])
        y.append(a[1])
        x.append(dataSet[near_point[i]][0])
        y.append(dataSet[near_point[i]][1])
        plt.plot(x, y, color='r', linewidth=0.5)
        # print(a, dataSet[near_point[i]][:2])
    plt.show()
