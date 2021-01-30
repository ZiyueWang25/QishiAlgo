class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            n = -n
            x = 1 / x
        if n == 1:
            return x
        if n == 0:
            return 1
        n -= 1
        count = 1
        prev_x = x
        while n - count >= 0:
            x *= x
            n -= count
            count *= 2
        return x * self.myPow(prev_x, n)
