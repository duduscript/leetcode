# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dic = {}
        foo,rtn = None,None
        if head:
            dic[head.val] = 1
            rtn = ListNode(head.val)
            foo = rtn
        while head:
            if not head.val in dic:
                dic[head.val] = 1
                rtn.next = ListNode(head.val)
                rtn = rtn.next
            head = head.next
        return foo