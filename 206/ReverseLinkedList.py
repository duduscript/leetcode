# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        vals,p = [],head
        while p:
            vals.append(p.val)
            p = p.next
        p,pos = head,len(vals)-1
        while p:
            p.val = vals[pos]
            pos,p = pos-1,p.next
        return head