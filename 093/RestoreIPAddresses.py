class Solution(object):
    def restore(self, s, n, paths, path):
        if n == 0 and s == '':
            paths.append(path)
            return
        elif n == 0 or s == '':
            return
        for x in xrange(1,min(len(s),3)+1):
            if str(int(s[:x])) != s[:x] or int(s[:x]) > 255:
                break
            self.restore(s[x:],n-1,paths,path+[s[:x]])
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        paths = []
        if len(s) > 12 or len(s) <4:
            return paths
        self.restore(s, 4, paths, [])
        return map(lambda x:'.'.join(x),paths)