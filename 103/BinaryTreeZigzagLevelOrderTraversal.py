# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        level,head,queue,ans = -1,0,[[root,0]],[]
        while head != len(queue):
            node,l= queue[head]
            head += 1
            if node.left != None:
                queue.append([node.left,l+1])
            if node.right != None:
                queue.append([node.right,l+1])
            if l == level:
                ans[-1].append(node.val)
            else:
                ans.append([node.val])
                level += 1
        for i in xrange(len(ans)):
            if i % 2 == 1:
                ans[i] = ans[i][::-1]
        return ans