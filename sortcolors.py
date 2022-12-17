class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[0]
            less = [i for i in nums[1:]if i <= pivot]
            greater = [i for i in nums[1:]if i > pivot]
            return self.sortColors(less) + [pivot] + self.sortColors(greater)
    