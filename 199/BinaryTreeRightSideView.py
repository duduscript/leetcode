# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        q,level,rtn = Queue.Queue(),0,{}
        q.put((root,1))
        while not q.empty():
            node = q.get()
            if node[1] > level:
                level += 1
            rtn[level] = node[0].val
            if node[0].left:
                q.put((node[0].left,level+1))
            if node[0].right:
                q.put((node[0].right,level+1))
        return rtn.values()