class Solution:
    def findDuplicate(self, nums):
        # print(nums)
        slow = fast = nums[0]
        # print("Find intersection")
        while True:
            # print(slow, fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        # print("Find The point")
        while slow != fast:
            # print(slow, fast)
            slow = nums[slow]
            fast = nums[fast]
        return slow
