#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


# 数据准备
dataset = []
for line in open("data_knn.csv"):
    x, y, label = line.split(",")
    dataset.append([int(x), int(y), int(label)])
print(dataset)


# In[8]:


# 数据处理
train_datas = []
train_labels = []
for i in dataset:
    # print(i[0:2])
    train_datas.append(i[0:2])
    train_labels.append(i[-1])
print(train_datas)
print(train_labels)


# In[9]:


# 创建模型 k=3
knn = KNeighborsClassifier(n_neighbors=3)
# 开始训练模型
knn.fit(train_datas, train_labels)
print(knn.predict([[14,17]]))
print(knn.predict_proba([[14,17]]))


# In[11]:



for data in dataset:
    plt.scatter(data[0], data[1], marker='o', color='green', s=40, label='原始点')
a = [14, 17]
plt.scatter(a[0], a[1], marker='o', color='red', s=40, label='预测点')
plt.show()


# In[ ]:




