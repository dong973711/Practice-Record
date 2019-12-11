class Solution:
    def Power(self, base, exponent):
        # write code here
        mul = 1
        if exponent == 0:
            return 1
        if base == 0:
            return 0
        else:
            if exponent > 0:
                for i in range(0, exponent):
                    mul = mul * base
                return mul
            else:
                # print("指数为负数")
                for i in range(0, abs(exponent)):
                    mul = mul * base
                # print(mul)
                return 1/mul


s = Solution()
b = 2.1
e = -3
r = s.Power(b, e)
print(r)
