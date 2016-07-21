# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathFind(self, paths, path, root, sum):
        if sum == root.val and root.left == None and root.right == None:
            paths.append(path+[root.val])
            return
        if root.left != None:
            self.pathFind(paths,path+[root.val],root.left,sum-root.val)
        if root.right != None:
            self.pathFind(paths,path+[root.val],root.right,sum-root.val)
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = []
        if root != None:
            self.pathFind(paths,[],root,sum)
        return paths