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
        if not head or not head.next:
            return None

        slow,fast = head,head
        while fast and fast.next != None:
            slow = slow.next
            fast =fast.next.next
        
        tail = None
        temp = slow
        while temp :
            next_node = temp.next
            temp.next = tail
            tail = temp
            temp = next_node

        first = head
        second = tail
        while second.next:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2 
