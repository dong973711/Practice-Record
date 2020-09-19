# with open('data.csv', 'r') as f:
#      reader = csv.reader(f)
#      print(type(reader))
#      for read in reader:
#         print(read)

dataset = []
for line in open("data.csv"):
    x, y = line.split(",")   # 这部分读出来是字符串形式
    dataset.append([int(x),int(y)])  # 放入列表时把字符串改成数字形式

print(dataset)

import numpy as np
a = np.array([1,2,3])
print("a:", a)
b = np.tile(a, 1)
print("b:", b)
b = np.tile(a, 2) # 在列的方向重复两次
print("b:", b)
c = np.tile(a, (3, 2))   # 在行的方向重复3次，列的方向重复三2次
print("c:", c,type(c))

# d=[[1,2,3,4,5,6],
#    [1,2,3,4,5,6],
#    [1,2,3,4,5,6]]
# print("d",d,type(d))
#
# e = c-d
# print("e:",e, type(e))

f = np.sum(c,axis=1)  # axis=0行相加，axis=1列相加
print("f:", f, type(f))

list = []
for i in range(4):
    list.append([1,2,3])
print(list)
print(np.array(list))


g = np.argmax(c,axis=0)  # axic=1 按列找到最大值的下标
print(g)