class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtn = []
        for i in xrange(1,n+1):
            if i%15 == 0:
                rtn.append("FizzBuzz")
            elif i%3 == 0:
                rtn.append("Fizz")
            elif i%5 == 0:
                rtn.append("Buzz")
            else:
                rtn.append(str(i))
        return rtn