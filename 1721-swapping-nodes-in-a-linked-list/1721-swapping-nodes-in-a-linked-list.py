# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # temp = head
        # dummy = ListNode(0, head)
        # pre = dummy
        # count = 1
        # while temp:
        #     temp = temp.next
        #     pre = pre.next
        #     print(pre)
        #     count+=1
        #     if count == k:
        #         first = ListNode(temp.val, temp.next)
        #         temp = head
        #         continue
            
    
        if not head:
            return head

        first = head
        for i in range(k-1):
            first = first.next
        second = first
        temp = head
        while second.next:
            temp = temp.next
            second = second.next
        second = temp
        first.val, second.val = second.val , first.val
        return head


            