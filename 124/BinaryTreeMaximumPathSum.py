# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxRootPathSum(self, root):
        if root.left == None and root.right == None:
            return root.val,root.val
        elif root.left == None:
            half_r,wtho_r = self.maxRootPathSum(root.right)
            return max(root.val,half_r+root.val),max(root.val,half_r+root.val,wtho_r)
        elif root.right == None:
            half_l,wtho_l = self.maxRootPathSum(root.left)
            return max(root.val,half_l+root.val),max(root.val,half_l+root.val,wtho_l)
        else:
            half_r,wtho_r = self.maxRootPathSum(root.right)
            half_l,wtho_l = self.maxRootPathSum(root.left)
            return max(root.val,root.val+half_l,root.val+half_r),max(wtho_r,wtho_l,root.val+half_r,root.val+half_l,root.val+half_r+half_l)
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.maxRootPathSum(root))