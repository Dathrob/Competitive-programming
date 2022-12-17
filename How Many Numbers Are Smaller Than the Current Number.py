class Solution(object):
    def smallerNumbersThanCurrent(self, array):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smaller_list = []
        count = 0
        for i in range(len(array)):
            for j in range(len(array)):
                if i == j:
                    continue
                elif array[i] > array[j]:
                    count += 1
            smaller_list.append(count)
            count = 0
        return smaller_list