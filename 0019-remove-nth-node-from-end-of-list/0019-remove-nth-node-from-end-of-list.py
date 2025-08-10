# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # dummy = ListNode(0,head)

        # count = 0
        # temp = head
        # while temp:
        #     count+=1
        #     temp = temp.next

        # pre = dummy
        # for i in range(count-n):
        #     pre = pre.next
        # pre.next = pre.next.next
        # return dummy.next

        slow = head
        fast = head
        i=1
        for i in range(n):
            if fast is None:
                return head
            fast = fast.next
            
        if fast == None:
            head = head.next
            return head
            
        while fast.next:
            slow =slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head 