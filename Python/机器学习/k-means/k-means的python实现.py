import random
import matplotlib.pyplot as plt

# 创建数据集
def createDataSet():
    return [[1, 1], [1, 2], [2, 1], [6, 4], [6, 3], [5, 4]]


# k-means算法
def kmeans(dataSet, k):
    centerCores = random.sample(dataSet, k)
    # centerCores = [[1,2], [2,3]]
    print("随机质心：", centerCores)
    changed, newCenterCore = updateCenterCore(dataSet, centerCores, k)
    print("第1次改变量：", changed)
    print("第1次新质心：", newCenterCore)
    c = 2
    while changed != 0:
        print("--------------------------------")
        changed, newCenterCore = updateCenterCore(dataSet, newCenterCore, k)
        print(c, "改变量：", changed)
        print(c, "新质心：", newCenterCore)
        c = c + 1

    return changed, newCenterCore


# 更新质心
def updateCenterCore(dataSet, centerCores, k):
    # 求各点到质心的距离
    calcDisList = calcDis(dataSet, centerCores, k)
    print(calcDisList)
    # 求新的质心
    l = len(dataSet)
    minClass = []
    maxClass = []
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    for i in range(l):
        if calcDisList[i] > calcDisList[i + l]:
            maxClass.append(dataSet[i])
            print("max", dataSet[i])
        else:
            minClass.append(dataSet[i])
            print("min", dataSet[i])
    for i in range(len(maxClass)):
        maxX = maxX + maxClass[i][0]
        maxY = maxY + maxClass[i][1]
    print(maxX, maxY, len(maxClass))
    for i in range(len(minClass)):
        minX = minX + minClass[i][0]
        minY = minY + minClass[i][1]
    print(minX, minY, len(minClass))
    # newCenterCores = [[minX/len(minClass),minY/len(minClass)], [maxX/len(maxClass), maxY/len(maxClass)]]
    newCenterCores = [[round(minX / len(minClass), 2), round(minY / len(minClass), 2)],
                      [round(maxX / len(maxClass), 2), round(maxY / len(maxClass), 2)]]
    # print("新质心：", newCenterCores)
    changed = 0
    for i in range(k):
        changed = changed + (((newCenterCores[i][0] - centerCores[i][0])** 2 + (
                    newCenterCores[i][1] - centerCores[i][1])** 2) ** 0.5)
    return changed, newCenterCores


# 计算各点到质心的距离
def calcDis(dataSet, centerCores, k):
    calcList = []
    for j in range(k):
        for i in range(len(dataSet)):
            calcList.append((((centerCores[j][0] - dataSet[i][0]) + (centerCores[j][1] - dataSet[i][1])) ** 2) ** 0.5)
    # print("各点与质心的距离：",calcList)
    return calcList


if __name__ == '__main__':
    startList = createDataSet()
    for i in range(len(startList)):
        plt.scatter(startList[i][0], startList[i][1],marker='o', color='green', s=40, label='原始点')
    print("原始数据点：", startList)
    changed, newCenterCores = kmeans(startList, 2)
    for i in range(len(newCenterCores)):
        plt.scatter(newCenterCores[i][0], newCenterCores[i][1], marker='x', color='red', s=50, label='质心')
    plt.show()
