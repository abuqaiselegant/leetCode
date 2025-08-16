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

        # 1) Find k-th from start
        first = head
        for _ in range(k - 1):
            first = first.next

        # 2) Find k-th from end using two-pointer technique
        fast = head
        for _ in range(k):
            fast = fast.next  # move k steps ahead

        second = head
        while fast:
            fast = fast.next
            second = second.next

        # 3) Swap values
        first.val, second.val = second.val, first.val
        return head
        

            