class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return map(int,list(str(int(reduce(lambda x,y:x+str(y),digits,''))+1)) )