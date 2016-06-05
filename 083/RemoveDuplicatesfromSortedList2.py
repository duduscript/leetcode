class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        if head.val == head.next.val:
            head = self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head