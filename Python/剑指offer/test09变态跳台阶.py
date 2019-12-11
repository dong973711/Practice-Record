class Solution:
    def jumpFloorII(self, number):
        # write code here
        f = [0,1,2]
        for i in range(3,number+1):
            f.append(2*f[i-1])
        return f[number]

s = Solution()
print(s.jumpFloorII(5))
