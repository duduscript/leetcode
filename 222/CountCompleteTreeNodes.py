# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getLength(self,root,flag):
        count,tmp = 0,root
        while tmp != None:
            count += 1
            tmp = tmp.left if flag == 0 else tmp.right
        return count
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        ln,mn,rn = self.getLength(root,0),1+self.getLength(root.left,1),self.getLength(root,1)
        if ln == rn:
            return pow(2,ln)-1
        else:
            return pow(2,mn-1) + (self.countNodes(root.right) if ln == mn else self.countNodes(root.left))