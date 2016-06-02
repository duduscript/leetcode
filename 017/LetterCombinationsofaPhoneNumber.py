dic = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
}
def func(c,a):
    rtn = []
    if len(a) == 0:
        for char in dic[c]:
            rtn.append(char)
    else:
        for s in a:
            for char in dic[c]:
                rtn.append(s+char)
    return rtn
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        for i in digits:
            ans = func(i,ans)
        return ans