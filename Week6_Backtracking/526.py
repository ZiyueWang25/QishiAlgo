class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        nums = list(range(1, n+1))
        def back(place, left):
            nonlocal res
            if place == n+1:
                res += 1
                return
            for i, num in enumerate(left):
                if num % place == 0 or place % num == 0:
                    back(place+1, left[:i] + left[i+1:])
        back(1, nums)
        return res