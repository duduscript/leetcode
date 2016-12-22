class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return max(map(lambda node:min(len(citations)-node[0],node[1]),enumerate(sorted(citations)))) if len(citations) else 0