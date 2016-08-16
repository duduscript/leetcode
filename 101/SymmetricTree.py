# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isMirror(self, r1, r2):
        if r1 == None and r2 == None:
            return True
        elif r1 == None or r2 == None:
            return False
        else:
            return r1.val == r2.val and self.isMirror(r1.left,r2.right) and self.isMirror(r1.right,r2.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True if root == None else self.isMirror(root.left,root.right)