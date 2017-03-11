# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getK(self, head, k):
        if head == None:
            return None
        return head if k == 1 else self.getK(head.next,k-1)
    def reverseK(self, head, k):
        if k == 1:
            return head,head
        h,t = self.reverseK(head.next,k-1)
        t.next = head
        return h,head
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        nextK = self.getK(head,k)
        if nextK == None:
            return head
        else:
            p = nextK.next
            h,t = self.reverseK(head,k)
            t.next = self.reverseKGroup(p,k)
            return h