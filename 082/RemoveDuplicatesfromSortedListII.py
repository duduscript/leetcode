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
        dic,h,num = {},head,0
        while h:
            if h.val in dic:
                dic[h.val] += 1
            else:
                dic[h.val] = 1
            h = h.next
        h,g,bar = head,None,None
        while h:
            if dic[h.val] == 1:
                if g == None:
                    g = ListNode(h.val)
                    bar = g
                else:
                    g.next = ListNode(h.val)
                    g = g.next
            h = h.next
        return bar