class Solution:
    def isPowerOfThree(self, num: int) -> bool:
        if (((num / 3) == 1) or num == 1):
            return True
        elif num % 3 != 0 or num == 0:
            return False
        else:
            return self.isPowerOfThree(num/3)
