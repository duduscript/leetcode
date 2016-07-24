# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepth(self, root):
        return 0 if root == None else 1+max(self.deepth(root.left),self.deepth(root.right))
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True if root == None else self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.deepth(root.left)-self.deepth(root.right)) <= 1