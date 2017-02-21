class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s <= 10:return []
        rtn,seq = set(),sorted(map(lambda i:s[i:i+10],xrange(len(s)-9)))
        for i in xrange(1,len(seq)):
            if seq[i] == seq[i-1] and seq[i] not in rtn:
                rtn.add(seq[i])
        return list(rtn)