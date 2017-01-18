# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.trees = {0:[None]}
    def TreePlus(self, root, n):
        if root == None:
            return
        root.val += n
        self.TreePlus(root.left, n)
        self.TreePlus(root.right, n)
    def InOnderMap(self, tree):
        pass
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n in self.trees:
            return trees[n]
        lefts,right,rtn = [],[],[]
        for i in xrange(n):
            if i in self.trees:
                lefts = self.trees[i]
            else:
                self.trees[i] = self.generateTrees(i)
                lefts = self.trees[i] 
            if n-1-i in self.trees:
                rights = self.trees[n-1-i]
            else:
                self.trees[n-1-i] = self.generateTrees(n-1-i)
                rights = self.trees[n-1-i]
            for left in lefts:
                for right in rights:
                    root = TreeNode(i+1)
                    root.left = left
                    root.right = right
                    rtn.append(root)
        return map(self.InOrderMap,rtn)