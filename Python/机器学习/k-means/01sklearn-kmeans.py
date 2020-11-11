#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# In[4]:


# 加载数据
dataset = []
for line in open("data_kmeans.csv"):
    x, y = line.split(",")
    dataset.append([int(x), int(y)])
print(dataset)


# In[13]:


k=3
# 训练模型
model = KMeans(n_clusters=k)
model.fit(dataset)
# 分类中心点坐标
centers = model.cluster_centers_
print(center)


# In[15]:


# 预测结果
result = model.predict(dataset)
print(result)


# In[42]:



# 用不同的颜色绘制数据点
mark = ['or', 'og', 'ob']
for i,d in enumerate(dataset):
    plt.plot(d[0], d[1], mark[result[i]])
# 画出各分类点的中心点
mark = ['*b', '*r', '*g'] # 为了凸显质心，把每个簇的质心颜色换成其他的
for i, center in enumerate(centers):
    plt.plot(center[0], center[1], mark[i], markersize=20)


# In[ ]:




