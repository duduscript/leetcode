# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if head == None:
            return None
        else:
            p,q = head,head.next
            while q:
                if q.val == val:
                    p.next = q.next
                    q = q.next
                else:
                    p,q = p.next,q.next
            return head