import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt


def createDataSet():
    dataset = []
    for line in open("data.csv"):
        x, y = line.split(",")
        dataset.append([int(x), int(y)])
    return dataset
    # return [[1, 1], [1, 2], [2, 1], [6, 4], [6, 3], [5, 4]]


def kmeans(dataSet, k):
    # 随机取质心
    center_cores = random.sample(dataSet, k)
    print("随机质心为：", center_cores)
    # 更新质心 直到变化量全为0
    changed, new_center_core = updateCenterCore(dataSet, center_cores, k)
    print("第1次改变量：", changed)
    print("第1次新质心：", new_center_core)
    c = 2
    while np.any(changed != 0):
        print("--------------------------------")
        changed, new_center_core = updateCenterCore(dataSet, new_center_core, k)
        print(c, "改变量：", changed)
        print(c, "新质心：", new_center_core)
        c = c + 1

    # 根据质心计算每个集群
    cluster = []
    clalist = calcDis(dataSet, new_center_core, k)  # 调用欧拉距离
    # print("fnjsanvjd:",clalist)
    minDistIndices = np.argmin(clalist, axis=1)
    print("minDistIndices:",minDistIndices)
    for i in range(k):
        cluster.append([])
    for i, j in enumerate(minDistIndices):  # enymerate()可同时遍历索引和遍历元素
        cluster[j].append(dataSet[i])
        # print(i,j)
    # print("mmasdognjangosanmkjldk:",cluster)
    return cluster, new_center_core


def calcDis(dataSet, center_cores, k):
    clalist = []
    # print(dataSet[1], center_cores[1])
    for data in dataSet:
        diff = np.tile(data, (k,
                              1)) - center_cores  # 相减   (np.tile(a,(2,1))就是把a先沿x轴复制1倍，即没有复制，仍然是 [0,1,2]。 再把结果沿y方向复制2倍得到array([[0,1,2],[0,1,2]]))
        squaredDiff = diff ** 2  # 平方
        squaredDist = np.sum(squaredDiff, axis=1)  # 和  (axis=1表示行，按行相加)
        distance = squaredDist ** 0.5  # 开根号
        clalist.append(distance)
    # print("clalist:", clalist)
    clalist = np.array(clalist)  # 返回一个每个点到质点的距离len(dateSet)*k的数组
    # print("np.array(clalist):", clalist)
    return clalist


def updateCenterCore(dataSet, center_cores, k):
    # 计算样本到质心的距离
    clalist = calcDis(dataSet, center_cores, k)
    # 分组并计算新的质心
    minDistIndices = np.argmin(clalist, axis=1)  # axis=1 表示求出每行的最小值的下标
    new_center_core = pd.DataFrame(dataSet).groupby(
        minDistIndices).mean()  # DataFramte(dataSet)对DataSet分组，groupby(min)按照min进行统计分类，mean()对分类结果求均值
    new_center_core = new_center_core.values
    # 计算变化量
    changed = new_center_core - center_cores
    return changed, new_center_core

if __name__ == '__main__':
    start_list = createDataSet()
    # for i in range(len(start_list)):
    #     plt.scatter(start_list[i][0], start_list[i][1], marker='o', color='green', s=40, label='原始点')
    # print("原始数据点：", start_list)
    cluster, new_center_cores = kmeans(start_list, 3)
    color = ['green', 'red', 'blue']
    count = 0
    for zu in cluster:
        for j in zu:
            plt.scatter(j[0], j[1], marker='o', color=color[count], s=40, label='原始点')
        count = count+1
    for i in range(len(new_center_cores)):
        plt.scatter(new_center_cores[i][0], new_center_cores[i][1], marker='x', color='red', s=50, label='质心')
    # print("计算结果为：",cluster, new_center_cores)
    plt.show()