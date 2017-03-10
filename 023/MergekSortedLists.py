# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import Queue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = Queue.PriorityQueue()
        rtn,pnew = None,None
        for i in xrange(len(lists)):
            if lists[i]:
                q.put([lists[i].val,i])
                lists[i] = lists[i].next
        while not q.empty():
            m = q.get()
            if rtn == None:
                pnew = rtn = ListNode(m[0])
            else:
                pnew.next = ListNode(m[0])
                pnew = pnew.next
            if lists[m[1]]:
                q.put([lists[m[1]].val,m[1]])
                lists[m[1]] = lists[m[1]].next
        return rtn
                