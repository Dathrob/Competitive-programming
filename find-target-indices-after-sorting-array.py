class Solution(object):
    def sort(self, array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
            return self.sort(less) + [pivot] + self.sort(greater)
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted = self.sort(nums)
        apperance = []
        for i in range(len(nums)):
            if sorted[i] == target:
                print("i is ",i)
                apperance.append(i)
        return apperance