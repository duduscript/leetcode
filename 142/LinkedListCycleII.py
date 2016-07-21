# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head != None and head.next != None:
            s,f = head,head.next
        else:
            return None
        while s != f:
            if f == None or f.next == None:
                return None
            s,f = s.next,f.next.next
        if s != head:
            s,f = s.next,head
            while s != f:
                s,f = s.next,f.next
        return s