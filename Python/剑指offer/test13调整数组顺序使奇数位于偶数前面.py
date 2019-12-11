# -*- coding:utf-8 -*-
class Solution1:
    # 开辟新数组
    def reOrderArray(self, array):
        # write code here
        rst = []
        for i in array:
            if i % 2 == 1:
                rst.append(i)
        for i in array:
            if i % 2 == 0:
                rst.append(i)
        return rst


class Solution2:
    # 利用冒泡排序
    def reOrderArray(self, array):
        l = len(array)
        flag = True
        while l and flag:
            flag = False
            for i in range(len(array) - 1):
                if array[i] % 2 == 0 and array[i + 1] % 2 == 1:
                    t = array[i]
                    array[i] = array[i + 1]
                    array[i + 1] = t
                    flag = True
            l -= 1
        return array


s = Solution2()
t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(s.reOrderArray(t))
