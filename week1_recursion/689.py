class Solution:
    def canPartitionKSubsets(self, nums, k):
        if len(nums) < k:
            return False
        num_sum = sum(nums)
        if num_sum % k != 0:
            return False
        nums.sort(reverse=True)
        target = [num_sum // k] * k

        def dfs(pos):
            if pos == len(nums):
                return True
            for i in range(k):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(pos + 1):
                        return True
                    target[i] += nums[pos]
            return False
        return dfs(0)