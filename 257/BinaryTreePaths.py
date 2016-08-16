# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePathsSearch(self, root, paths, path, isRoot):
        if isRoot == False:
            path += '->' +str(root.val)
        if root.left == None and root.right == None:
            paths.append(path)
        else:
            if root.left:
                self.binaryTreePathsSearch(root.left, paths, path, False)
            if root.right:
                self.binaryTreePathsSearch(root.right, paths, path, False)
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        paths = []
        if root == None:
            return paths
        self.binaryTreePathsSearch(root, paths, str(root.val), True)
        return paths