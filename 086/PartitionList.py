# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def makeList(self, l):
        if len(l) == 0:
            return None
        node = ListNode(l[0])
        node.next = self.makeList(l[1:])
        return node
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return head
        p,bar,foo = head,[],[]
        while p:
            if p.val < x:
                bar.append(p.val)
            else:
                foo.append(p.val)
            p = p.next
        bar.extend(foo)
        return self.makeList(bar)
