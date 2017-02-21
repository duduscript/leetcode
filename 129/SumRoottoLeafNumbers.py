# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findNumbers(self, root, num, nums):
        if root == None:
            nums.append(num)
        elif root.left == None and root.right == None:
            nums.append(num+str(root.val))
        elif root.left and root.right:
            self.findNumbers(root.left,num+str(root.val),nums)
            self.findNumbers(root.right,num+str(root.val),nums)
        elif root.left:
            self.findNumbers(root.left,num+str(root.val),nums)
        else:
            self.findNumbers(root.right,num+str(root.val),nums)
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []
        self.findNumbers(root,'0',nums)
        return sum(map(lambda x:int(x),nums))
