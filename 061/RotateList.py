# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow,fast = head,head.next
        while fast != None and fast.next != None:
            if slow == fast:
                return True
            slow,fast = slow.next,fast.next.next
        return False