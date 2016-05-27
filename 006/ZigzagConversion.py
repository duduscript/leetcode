class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i = 0
        size = len(s)
        l = []
        for x in range(0,numRows):
            l.append([])
        down = False
        while i < size:
            if i+numRows-1 > size:
                right = size
            else:
                right = i+numRows-1
            if down == False:
                op = 0
                for j in range(i,right):
                    l[op].append(s[j])
                    op += 1
                down = True
            else:
                op = numRows - 1
                for j in range(i,right):
                    l[op].append(s[j])
                    op -= 1
                down = False
            i = right
        r = ''
        for i in l:
            for j in i:
                r += j
        return r