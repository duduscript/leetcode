# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h,l,even = None,None,True
        while head:
            if even:
                if l == None:
                    h = l = ListNode(head.val)
                    head = head.next
                else:
                    l.next = ListNode(head.val)
                    l,head = l.next,head.next
                even = False
            else:
                l.val,l.next = head.val,ListNode(l.val)
                l,even,head = l.next,True,head.next
        return h