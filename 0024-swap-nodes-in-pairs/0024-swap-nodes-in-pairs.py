# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if temp==None:
            return None
        if temp.next:
            head = temp.next
        
        pre = None
        while temp and temp.next:
            first = temp
            second = temp.next
            following = second.next

            second.next = first
            first.next =following
            
            if pre:
                pre.next = second
            pre = first
            temp = following
        return head

        

        