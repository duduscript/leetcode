class Solution(object):
    def getKey(self,s):
        t = [0]*26
        for c in s:
            t[ord(c)-ord('a')] += 1
        return t
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic,keys,foo = {},[],[]
        for x in strs:
            t = self.getKey(x)
            keys.append([t,x])
        keys = sorted(keys,key=lambda x:x[0])
        for i in xrange(len(keys)):
            if i == 0 or keys[i][0] != keys[i-1][0]:
                foo.append([keys[i][1] ])
            else:
                foo[-1].append(keys[i][1])
        return foo