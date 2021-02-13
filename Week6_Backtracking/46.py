from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def back(temp, left):
            nonlocal res
            if not left:
                res.append(temp)
                return
            for i in range(len(left)):
                back(temp + [left[i]], left[:i] + left[i + 1:])

        back([], nums)
        return res
