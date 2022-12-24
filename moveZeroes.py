class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        let me count the number of non zeros
        and count the number of zeros
        """
        zeros = 0
        non_zeros  = 0
        counter = 0
        reverse_counter = len(nums)-1
        copy_of_reverse_counter = reverse_counter
        for i in nums:
            if i != 0:
                non_zeros += 1
                nums[counter] = i
                counter +=1
            else:
                zeros += 1
        while reverse_counter > copy_of_reverse_counter - zeros:
            nums[reverse_counter] = 0
            reverse_counter -=1
        return nums
            



