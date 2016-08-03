# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        path = self.inorderTraversal(root.left)
        path.append(root.val)
        path.extend(self.inorderTraversal(root.right))
        return path
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        path = self.inorderTraversal(root)
        for i in xrange(1,len(path)):
            if path[i] <= path[i-1]:
                return False
        return True