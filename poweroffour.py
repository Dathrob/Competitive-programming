class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if (((num / 4) == 1) or num == 1):
            return True
        elif num % 4 != 0 or num == 0:
            return False
        else:
            return self.isPowerOfFour(num/4)