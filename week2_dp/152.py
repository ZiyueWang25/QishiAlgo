class Solution:
    def maxProduct(self, nums):
        imax = imin = r = nums[0]
        for i in range(1, len(nums)):
            imax, imin = max(nums[i], imax * nums[i], imin * nums[i]),\
                         min(nums[i], imin * nums[i], imax * nums[i])
            r = max(r, imax)
        return r