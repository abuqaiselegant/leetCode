# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head is not None and head.val == val:
            head = head.next
        temp = head
        pre = None
        while temp is not None: 
            if temp.val == val:
                pre.next = temp.next
            else:
                pre = temp
            temp = temp.next
        return head
