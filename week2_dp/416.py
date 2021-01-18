class Solution:
    def canPartition(self, nums) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        dp = [False] * (target+1)
        dp[0] = True
        ps = [0]
        for num in nums:
            new_ps = []
            for p in ps:
                if p + num > target:
                    continue
                else:
                    if not dp[p+num]:
                        dp[p+num] = True
                        new_ps.append(p+num)
            ps.extend(new_ps)
        return dp[-1]