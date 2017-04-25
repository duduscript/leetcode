class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        m,length,table,nb = 0,[len(x) for x in words],[0]*26,[0]*len(words)
        for i in xrange(26):
            table[i] = set()
        for i in xrange(len(words)):
            nb[i] = set(range(len(words)))
        for i in xrange(len(words)):
            for c in words[i]:
                table[ord(c)-ord('a')].add(i)
        for s in table:
            for i in s:
                nb[i] -= s
        for i in xrange(len(nb)):
            for j in nb[i]:
                m = max(m,length[i]*length[j])
        return m