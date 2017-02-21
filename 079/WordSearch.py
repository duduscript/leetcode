class Solution(object):
    def search(self, board, word, table, x, y):
        if board[x][y] != word[0] or table[x][y]:
            return False
        if len(word) == 1:
            return True
        table[x][y] = 1
        if x != 0 and self.search(board, word[1:], table, x-1, y):
            return True
        if x+1 != len(board) and self.search(board, word[1:], table, x+1, y):
            return True
        if y != 0 and self.search(board, word[1:], table, x, y-1):
            return True
        if y+1 != len(board[0]) and self.search(board, word[1:], table, x, y+1):
            return True
        table[x][y] = 0
        return False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        table = []
        for i in xrange(len(board)):
            table.append([0]*len(board[0]))
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.search(board,word,table,i,j):
                    return True
        return False