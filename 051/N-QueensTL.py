class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        return [['.'*pos+'Q'+'.'*(n-pos-1) for pos in vec] for vec in [x for x in __import__('itertools').permutations(xrange(n)) if n ==len(set(x[i]+i for i in x)) == len(set(x[i]-i for i in x))]]