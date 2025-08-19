# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Dummy node before the real head
        dummy = ListNode(float('-inf'))
        dummy.next = head

        # The sorted part starts with the first node
        last_sorted = head
        curr = head.next

        while curr:
            if curr.val >= last_sorted.val:
                # Already in correct position
                last_sorted = last_sorted.next
            else:
                # Find where to insert curr
                prev = dummy
                while prev.next and prev.next.val < curr.val:
                    prev = prev.next

                # Relink: insert curr after prev
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr

            # Move forward
            curr = last_sorted.next

        return dummy.next