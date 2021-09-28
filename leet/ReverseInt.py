class Solution:
    def reverse(self, x: int) -> int:
        value = 0

        if x > 0:
            value = int(str(x)[::-1])
        else:
            value = (-1) * int(str(x*(-1))[::-1])

        if value not in range(-2**31, 2**31):
            value = 0

        return value 

sol = Solution()
x = 10
print(sol.reverse(x))
