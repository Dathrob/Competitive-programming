class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        array = []
        for i in range(1,n+1):
            print(i)
            if i % 3 == 0:
                if i % 5 == 0:
                    array.append("FizzBuzz")
                else:
                    array.append("Fizz")
            elif i % 5 == 0:
                array.append("Buzz")
            else:
                i = str(i)
                array.append(i)
        return array