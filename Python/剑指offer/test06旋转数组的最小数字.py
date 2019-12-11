class Solution:
    def minNumberInRotateArray(self, rotateArray):
        l = len(rotateArray)
        if l == 0:
            return 0

        for i in rotateArray:
            if rotateArray[0] > i:
                return i
        return rotateArray[0]


s = Solution()
t = [3, 4, 5, 1, 2]
min = s.minNumberInRotateArray(t)
print(min)
