# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        count = 0
        dummy = ListNode(0, head)
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n+=1
        k%=n
        if k ==0:
            return head
        
        while count<=k-1:
            temp =head
            pre = None
            while temp.next:
                pre = temp
                temp = temp.next
    
            pre.next = None
            temp.next = head
            head = temp
            count +=1
            
            
        return head