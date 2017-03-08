class Solution(object):
    def getpowten(self,n):
        if n == 0:
            return 1
        return (self.getpowten(n-1)-1)*10+pow(10,n-1)+1
    def getnpowten(self,n):
        zeros,head = len(str(n))-1,int(str(n)[0])
        if head == 0:
            return 0
        elif head == 1:
            return self.getpowten(zeros)
        else:
            return (self.getpowten(zeros)-1)*head+pow(10,zeros)
    def count(self, rg):
        left,right,i = rg
        if left == 0:
            return self.getnpowten(right)
        else:
            return len(filter(lambda x:x=='1',str(left)[:i]))*(right-left)+self.count((0,right-left,0))
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        elif n<10:
            return 1
        else:
            nums = map(lambda x:int(x[1])*pow(10,x[0]),enumerate(list(str(n))[::-1]))[::-1]
            nums = [0]+map(lambda x:sum(nums[:x+1]),xrange(len(nums)))
            return sum(map(self.count,map(lambda i:(nums[i],nums[i+1],i),xrange(len(nums)-1))))