class Solution:
    def fib(self, num: int) -> int:
        if (num <= 1):
            return num
        else:
            return self.fib(num-1) + self.fib(num-2)