class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        pos,la,lb,r = 0,len(a)-1,len(b)-1,[]
        while la >= 0 and lb >= 0:
            tmp = ord(a[la]) + ord(b[lb]) - ord('0')*2 + pos
            pos = 1 if tmp ==2 or tmp ==3 else 0
            r.append(tmp%2)
            la,lb = la-1,lb-1
        while la >= 0:
            tmp = ord(a[la]) - ord('0') + pos
            pos = 1 if tmp == 2 else 0
            r.append(tmp%2)
            la -= 1
        while lb >= 0:
            tmp = ord(b[lb]) - ord('0') + pos
            pos = 1 if tmp == 2 else 0
            r.append(tmp%2)
            lb -= 1
        if pos == 1:
            r.append(1)
        return ''.join(map(str,r))[::-1]