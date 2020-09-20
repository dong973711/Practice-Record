import csv
import numpy as np
import matplotlib.pyplot as plt


def createDataSet():
    dataset = []
    for line in open("data.csv"):
        x, y, label = line.split(",")
        dataset.append([int(x), int(y), int(label)])
    return dataset


# 计算各点到预测点的距离
def calcDis(dataSet, socuse, k):
    calcList = []
    for i in range(len(dataSet)):
        calcList.append(
            (((socuse[0] - dataSet[i][0]) ** 2 + (socuse[1] - dataSet[i][1]) ** 2) ** 0.5))
    # print("各点与质心的距离：",calcList)
    calcList = np.array(calcList)
    dis_sort_index = np.argsort(calcList)  # 排序并且得到的是下标
    dis_sort_index_near = dis_sort_index[0:k]  # 取得前k个下标
    for i in dis_sort_index_near:   # 查看前k个到底是哪一类
        print(dataSet[i])
    # print(dis_sort_index_near)
    # labels = []
    counts = [0, 0, 0]  # 统计前k名中三个标签出现的次数
    for i in range(k):
        # labels.append(dataSet[dis_sort_index_near[i]])
        # print(dataSet[dis_sort_index_near[i]][2])
        counts[dataSet[dis_sort_index_near[i]][2]] += 1
    print(counts)
    max_label = 0
    max_value = 0
    for i in range(3):
        if counts[i] > max_value:
            max_value = counts[i]
            max_label = i

    return max_label


if __name__ == '__main__':
    dataSet = createDataSet()
    for data in dataSet:
        plt.scatter(data[0], data[1], marker='o', color='green', s=40, label='原始点')
    a = [14, 17]
    plt.scatter(a[0], a[1], marker='o', color='red', s=40, label='预测点')
    plt.show()
    b = calcDis(dataSet, a, 5)
    print(a, "被预测为的类别是:", b)
