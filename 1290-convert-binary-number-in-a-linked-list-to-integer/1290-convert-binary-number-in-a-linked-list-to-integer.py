# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        temp = head
        sum = temp.val
        while temp.next:
            temp = temp.next
            sum= 2*sum +temp.val
        return sum
