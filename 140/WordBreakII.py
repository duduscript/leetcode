class Solution(object):
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if set(s) & set(''.join(wordDict)) != set(s):
            return False,{}
        dic_head,table,max_len = {},[0]*len(s)+[1],max(map(len,wordDict))
        for word in wordDict:
            if word[0] not in dic_head:
                dic_head[word[0]] = set([word])
            else:
                dic_head[word[0]].add(word)
        for i in range(len(s))[::-1]:
            if s[i] not in dic_head:
                continue
            for j in xrange(i,min(len(s),i+max_len)):
                if s[i:j+1] not in dic_head[s[i]]:
                    continue
                else:
                    if table[j+1]:
                        table[i] = 1
        return table[0] == 1,dic_head
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ok,dic_head = self.wordBreak1(s, wordDict)
        if not ok:
            return []
        subwords = {}
        for i in range(len(s))[::-1]:
            subwords[i] = []
            if s[i] not in dic_head:
                continue
            for j in xrange(i,len(s)):
                if s[i:j+1] not in dic_head[s[i]]:
                    continue
                elif j+1 == len(s):
                    subwords[i].append([s[i:j+1]])
                elif len(subwords[j+1]):
                    for k in xrange(len(subwords[j+1])):
                        subwords[i].append([s[i:j+1]]+subwords[j+1][k])
        return map(lambda x:' '.join(x),subwords[0])