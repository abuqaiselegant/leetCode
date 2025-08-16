# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 1) length of list
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next

        # 2) base size and how many get +1
        q, r = divmod(n, k)

        # 3) split
        res, cur = [], head
        for i in range(k):
            part_head = cur
            size = q + (1 if i < r else 0)

            # advance to end of this part
            for _ in range(size - 1):
                if cur:
                    cur = cur.next

            # cut and move to next part
            if cur:
                nxt = cur.next
                cur.next = None
                cur = nxt

            res.append(part_head)

        return res
            
