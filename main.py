# 题库训练
# sum1 = 0
# for i in range(1, 101):
#     sum1 += i
# print("和为", sum1, "个数为", i)

# sum2 = 0
# for i in range(1, 113, 3):
#     sum2 += i
# print("1+4+7+10+13+…+112的和为", sum2)

# sum3 = 0
# for i in range(2, 101, 5):
#     sum3 += i

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)
            x = x[1:]
            x = x[::-1]
            x = int(x)
            x = -x
        else:
            x = str(x)
            x = x[::-1]
            x = int(x)
        if x > 2**31-1 or x < -2**31:
            return 0
        else:
            return x