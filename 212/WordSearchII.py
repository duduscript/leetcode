class Solution(object):
    def search(self, board, trie, ans, path, x, y):
        if '#' in trie:
            ans.append(path)
        if x<0 or y<0 or x>=len(board) or y>=len(board[0]) or board[x][y] not in trie:
            return
        ch = board[x][y]
        board[x][y] = '*'
        self.search(board,trie[ch],ans,path+ch,x+1,y)
        self.search(board,trie[ch],ans,path+ch,x-1,y)
        self.search(board,trie[ch],ans,path+ch,x,y+1)
        self.search(board,trie[ch],ans,path+ch,x,y-1)
        board[x][y] = ch
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie,ans = {},[]
        for word in words:
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t['#'] = '#'
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.search(board,trie,ans,'',i,j)
        return list(set(ans))