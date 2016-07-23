# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m != 1:
            head.next = self.reverseBetween(head.next,m-1,n-1)
            return head
        q,p = head,head.next
        while m != n:
            tmp = q
            q = p
            p = p.next
            q.next,m = tmp,m+1
        head.next = p
        return q