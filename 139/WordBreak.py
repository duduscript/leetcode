class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dic_head,table = {},[0]*len(s)+[1]
        if set(s) & set(''.join(wordDict)) != set(s):
            return False
        for word in wordDict:
            if word[0] not in dic_head:
                dic_head[word[0]] = set([word])
            else:
                dic_head[word[0]].add(word)
        for i in range(len(s))[::-1]:
            if s[i] not in dic_head:
                continue
            for j in xrange(i,len(s)):
                if s[i:j+1] not in dic_head[s[i]]:
                    continue
                else:
                    if table[j+1]:
                        table[i] = 1
        return table[0] == 1