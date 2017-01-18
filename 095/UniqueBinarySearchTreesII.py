# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.trees = {0:[None]}
    def copy(self, tree):
        if tree == None:return None
        root = TreeNode(tree.val)
        root.left = self.copy(tree.left)
        root.right = self.copy(tree.right)
        return root
    def InOrderTravel(self, tree, n=0):
        if tree == None:return n
        mid = self.InOrderTravel(tree.left,n)
        tree.val = mid+1
        return self.InOrderTravel(tree.right,mid+1)
    def InOrderTrip(self, copytree):
        tree = self.copy(copytree)
        self.InOrderTravel(tree,0)
        return tree
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        if n in self.trees:
            return map(self.InOrderTrip,self.trees[n])
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
        return map(self.InOrderTrip,rtn)
