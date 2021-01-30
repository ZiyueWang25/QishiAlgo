class Solution(object):
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            # 2N
            left = count = 0
            right = 1
            while left < len(nums):
                while (right < len(nums)) and ((nums[right] - nums[left]) <= guess):
                    right += 1
                count += right - left - 1
                left += 1
            return count >= k
        nums.sort() # NlogN
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            # log(k)
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo