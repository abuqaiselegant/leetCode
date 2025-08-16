# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        pre = dummy

        while pre.next and pre.next.next:
            first = pre.next
            second = first.next
            following  = second.next

            first.next = following
            second.next = first
            pre.next = second

            pre = first
        return dummy.next


        # temp = head
        # if temp==None:
        #     return None
        # if temp.next:
        #     head = temp.next
        
        # pre = None
        # while temp and temp.next:
        #     first = temp
        #     second = temp.next
        #     following = second.next

        #     second.next = first
        #     first.next =following
            
        #     if pre:
        #         pre.next = second
        #     pre = first
        #     temp = following
        # return head
        
        

        