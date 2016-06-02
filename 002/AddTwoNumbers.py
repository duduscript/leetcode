# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getNodeNum(l):
    var,pos = 0,1
    while l != None:
        var += pos * l.val
        pos *= 10
        l = l.next
    return var

def makeList(val):
    rtn = bar = ListNode(0)
    while True:
        bar.val = val%10
        val /= 10
        if val == 0:
            return rtn
        else:
            bar.next = ListNode(0)
            bar = bar.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return makeList(getNodeNum(l1)+getNodeNum(l2))