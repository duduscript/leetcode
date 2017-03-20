class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic_s,dic_ss,dic_t = {},{},{}
        for i in xrange(len(t)):
            if t[i] not in dic_t:
                dic_t[t[i]] = 0
            dic_t[t[i]] += 1
        for i in xrange(len(s)):
            if s[i] not in dic_t:
                continue
            if s[i] not in dic_s:
                dic_s[s[i]] = []
                dic_ss[s[i]] = {}
            dic_s[s[i]].append(i)
            dic_ss[s[i]][i] = len(dic_s[s[i]])-1
        if any(map(lambda c:c not in dic_s or dic_t[c]>len(dic_s[c]),dic_t.keys())):
            return ""
        left = mi = min(map(lambda k:dic_s[k][0],dic_s.keys()))
        right = ma = max(map(lambda k:dic_s[k][dic_t[k]-1],dic_s.keys()))
        while True:
            c = s[mi]
            if dic_t[c] == len(dic_s[c]) - dic_ss[c][mi]:
                break
            else:
                nx = dic_s[c][dic_ss[c][mi]+dic_t[c]]
                ma = max(ma,nx)
                mi = mi+1
                while s[mi] not in dic_s:
                    mi += 1
                if ma-mi<right-left:
                    left,right = mi,ma
        return s[left:right+1]