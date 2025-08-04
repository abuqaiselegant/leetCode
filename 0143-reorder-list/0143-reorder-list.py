# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        slow , fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        pre = None
        temp = slow
        while temp:
            nextNode = temp.next
            temp.next = pre
            pre = temp
            temp = nextNode
        
        first = head
        second = pre
        while second.next:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
