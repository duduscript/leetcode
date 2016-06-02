class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        length = longest = i = 0
        size = len(s)
        while i < size:
            if not s[i] in dic:
                dic[s[i]] = i
                length += 1
            else:
                if length > longest:
                    longest = length
                for j in range(i-length,dic[s[i]]):
                    dic.pop(s[j])
                length = i - dic[s[i]]
                dic[s[i]] = i
            i += 1
        if length > longest:
            longest = length
        return longest