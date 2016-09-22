# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return root
        elif root.left == None:
            root.next = None
        self.connect(root.left)
        self.connect(root.right)
        l,r = root.left,root.right
        while l != None:
            l.next = r
            l,r = l.right,r.left
        root.next = None