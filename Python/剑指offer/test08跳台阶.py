class Solution:
    def jumpFloor(self, number):
        f = [0, 1, 2]
        if number <= 2:
            return f[number]
        else:
            for i in range(3, number+1):
                f.append(f[i - 1] + f[i - 2])
            return f[number]


s = Solution()
print(s.jumpFloor(1))
print(s.jumpFloor(2))
print(s.jumpFloor(3))
print(s.jumpFloor(4))
print(s.jumpFloor(5))
