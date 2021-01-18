import bisect
import
class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1
        for i, num in enumerate(nums):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + 1) if num > nums[j] else dp[i]
                res = max(res, dp[i])
        return res

    def lengthOfLIS(self, nums):
        # NlogN
        n = len(nums)
        q = [nums[0]]
        res = 1
        for i in range(1, n):
            num = nums[i]
            place = bisect.bisect_left(q, num)
            if place == len(q):
                q.append(num)
            else:
                q[place] = num
            res = len(q)
        return res