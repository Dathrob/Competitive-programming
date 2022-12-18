class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer = []
        found_element = False
        for i in range (len(nums1)):
            for j in range(len(nums2)):
                if ((nums1[i]) == (nums2[j])):
                    for k in range(j,len(nums2)):
                        if (nums2[k] > nums2[j]):
                            answer.append(nums2[k])
                            found_element = True
                            break
                    if not found_element:
                        answer.append(-1)
                        break
                    elif found_element:
                        found_element = False
                        break


                            
                            
        return answer