# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self,head):
        init = None
        while head:
            tmp = head.next
            head.next = init
            init = head
            head = tmp
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:return
        slow = fast = ListNode(0)
        slow.next = head
        while fast.next and fast.next.next:
            slow,fast = slow.next,fast.next.next
        if fast.next:
            slow,fast = slow.next,fast.next
        self.reverse(slow.next)
        slow.next = None
        while fast:
            if fast == None:
                head.next = None
            p,q = head.next,fast.next
            fast.next = p
            head.next = fast
            head,fast = p,q