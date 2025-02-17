# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        pre = None
        while head is not None and head.val == val:
            head = head.next
            
        while temp is not None:
            pre = temp
            temp = temp.next
            if temp is not None  and temp.val == val:
                pre.next = temp.next
        return head
