class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) != 0 and s[0] == '0':
            return 0
        num = [1]
        for i in xrange(len(s)):
            if i == 0:
                num.append(1)
            elif (int(s[i-1]) >= 3 or int(s[i-1]) == 0) and int(s[i]) != 0:
                num.append(num[-1])
            elif 1 <= int(s[i-1]) <= 2 and int(s[i]) == 0:
                if i >= 1 and num[-1] != num[-2]:
                    num.append(num[-2])
                num.append(num[-1])
            elif int(s[i-1]) == 1 or (int(s[i-1]) == 2 and int(s[i]) <= 6):
                num.append(num[-1]+num[-2])
            elif int(s[i-1]) == 2:
                num.append(num[-1])
            else:
                return 0
        return 0 if len(s) == 0 else num[-1]