# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        odd,even = head,head.next
        odd_tail,even_tail = odd,even
        while even_tail.next and even_tail.next.next:
            odd_tail.next = even_tail.next
            even_tail.next = odd_tail.next.next
            odd_tail,even_tail = odd_tail.next,even_tail.next
        if even_tail.next:
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next
        odd_tail.next,even_tail.next = even,None
        return odd