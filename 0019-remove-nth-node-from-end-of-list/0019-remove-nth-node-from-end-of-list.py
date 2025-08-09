# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0,head)

        count = 0
        temp = head
        while temp:
            count+=1
            temp = temp.next

        pre = dummy
        for i in range(count-n):
            pre = pre.next
        pre.next = pre.next.next
        return dummy.next