class Solution(object):
    def getPath(self,path):
        pos,f,p = 0,'',[]
        for pos in xrange(len(path)):
            p = p+[f] if path[pos] == '/' and len(f) != 0 else p
            f = f + path[pos] if path[pos] != '/' else ''
        return p if len(f) == 0 else p +[f]
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack,pos = [],0
        path = self.getPath(path)
        for pos in xrange(len(path)):
            if path[pos] == '..' and len(stack) != 0:
                stack.pop()
            elif path[pos] != '..' and path[pos] != '.':
                stack.append(path[pos])
        return '/'+'/'.join(stack)