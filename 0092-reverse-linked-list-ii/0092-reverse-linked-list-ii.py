# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head
        
        x = ListNode(0, head)
        pre = x

        for i in range(left - 1):
            pre = pre.next

        curr = pre.next            
        prev = None
        count = 0
        while count < (right -left+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count+=1
        
        pre.next.next = curr
        pre.next = prev
        
        return x.next
            
        
                
            
        