import random
import matplotlib.pyplot as plt
import operator


# 创建数据集
def createDataSet():
    dataset = []
    for line in open("data.csv"):
        x, y = line.split(",")
        dataset.append([int(x), int(y)])
    return dataset
    # return [[1, 1], [1, 2], [2, 1], [6, 4], [6, 3], [5, 4]]


# k-means算法
def kmeans(dataSet, k):
    center_cores = random.sample(dataSet, k)
    # center_cores = [[1,2], [33,18], [50,70]]
    print("随机质心：", center_cores)
    changed, new_center_core = updateCenterCore2(dataSet, center_cores, k)
    print("第1次改变量：", changed)
    print("第1次新质心：", new_center_core)
    c = 2
    while changed != 0:
        print("--------------------------------")
        changed, new_center_core = updateCenterCore2(dataSet, new_center_core, k)
        print(c, "改变量：", changed)
        print(c, "新质心：", new_center_core)
        c = c + 1

    return changed, new_center_core


# 更新质心
def updateCenterCore(dataSet, centerCores, k):
    # 求各点到质心的距离
    calc_dis_list = calcDis(dataSet, centerCores, k)
    new_center_cores = []
    print(calc_dis_list)
    # 求新的质心
    l = len(dataSet)
    '''
    对个点进行分类，分到对应质点下面
    比较每个点对各个质点的距离，然后把各个点分到对应的质点簇，然后进行质点更新
    '''
    classfiy = []
    x = []
    for j in range(k):
        classfiy.append([])
    for i in range(l):
        min_val = calc_dis_list[i]
        min_indx = i
        t = i
        for j in range(k - 1):
            if min_val > calc_dis_list[t + l]:
                min_val = calc_dis_list[t + l]
                min_indx = t + l
                t = t + l
        classfiy[min_indx // l].append(dataSet[i])
    print(classfiy)
    print("----------------------------------")
    for i in range(k):
        minX = 0
        minY = 0
        for j in range(len(classfiy[i])):
            minX = minX + classfiy[i][j][0]
            minY = minY + classfiy[i][j][1]
        # print(minX / len(classfiy[i]), minY / len(classfiy[i]))
        if len(classfiy[i]) == 0:
            new_center_cores.append(centerCores[i])
        else:
            new_center_cores.append([minX / len(classfiy[i]), minY / len(classfiy[i])])
    print("新质心为:", new_center_cores)
    changed = 0
    for i in range(k):
        changed = changed + (((new_center_cores[i][0] - centerCores[i][0]) ** 2 + (
                new_center_cores[i][1] - centerCores[i][1]) ** 2) ** 0.5)
    return changed, new_center_cores


# 更新质心
def updateCenterCore2(dataSet, centerCores, k):
    # 求各点到质心的距离
    calc_dis_list = calc_point2centers(dataSet, centerCores, k)
    new_center_cores = []
    print(calc_dis_list)
    # 求新的质心
    l = len(dataSet)
    '''
    对个点进行分类，分到对应质点下面
    比较每个点对各个质点的距离，然后把各个点分到对应的质点簇，然后进行质点更新
    '''
    classfiy = []
    x = []
    for j in range(k):
        classfiy.append([])
    for i in range(l):
        min_val = calc_dis_list[i][0]
        class_index = 0
        for j in range(1, k):
            if min_val > calc_dis_list[i][j]:
                min_val = calc_dis_list[i][j]
                class_index = j
        classfiy[class_index].append(dataSet[i])
    print(classfiy)
    print("----------------------------------")
    for i in range(k):
        minX = 0
        minY = 0
        for j in range(len(classfiy[i])):
            minX = minX + classfiy[i][j][0]
            minY = minY + classfiy[i][j][1]
        # print(minX / len(classfiy[i]), minY / len(classfiy[i]))
        if len(classfiy[i]) == 0:
            new_center_cores.append(centerCores[i])
        else:
            new_center_cores.append([minX / len(classfiy[i]), minY / len(classfiy[i])])
    print("新质心为:", new_center_cores)
    changed = 0
    for i in range(k):
        changed = changed + (((new_center_cores[i][0] - centerCores[i][0]) ** 2 + (
                new_center_cores[i][1] - centerCores[i][1]) ** 2) ** 0.5)
    return changed, new_center_cores

# 计算各点到质心的距离
def calcDis(dataSet, centerCores, k):
    calcList = []
    for j in range(k):
        for i in range(len(dataSet)):
            calcList.append(
                (((centerCores[j][0] - dataSet[i][0]) ** 2 + (centerCores[j][1] - dataSet[i][1]) ** 2) ** 0.5))
    # print("各点与质心的距离：",calcList)
    return calcList


# 计算距离
def calc_dis(point, center):
    return (((center[0] - point[0]) ** 2 + (center[1] - point[1]) ** 2) ** 0.5)


# 计算各节点到各质心的距离并放入calcList列表
def calc_point2centers(dataset, centerCores, k):
    calcList = []
    for i in range(len(dataset)):
        calcList.append([])
        for j in range(k):
            calcList[i].append((calc_dis(dataset[i], centerCores[j])))
    return calcList


if __name__ == '__main__':
    startList = createDataSet()
    for i in range(len(startList)):
        plt.scatter(startList[i][0], startList[i][1], marker='o', color='green', s=40, label='原始点')
    print("原始数据点：", startList)
    changed, new_center_cores = kmeans(startList, 3)
    for i in range(len(new_center_cores)):
        plt.scatter(new_center_cores[i][0], new_center_cores[i][1], marker='x', color='red', s=50, label='质心')
    plt.show()
