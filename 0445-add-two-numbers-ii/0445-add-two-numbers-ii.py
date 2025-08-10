# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        s1 = []
        s2 = []

        temp= l1
        while temp:
            s1.append(temp.val)
            temp = temp.next
        temp = l2
        while temp:
            s2.append(temp.val)
            temp = temp.next
        
        total = 0
        carry = 0
        head = None
        while s1 or s2 or carry:
            x= s1.pop() if s1 else 0
            y= s2.pop() if s2 else 0
            total = x+y+carry
            digit = total%10
            carry = total//10

            node = ListNode(digit)
            node.next = head
            head = node
        return head






        # def reverse(head):
        #     pre = None
        #     temp = head
        #     while temp:
        #         nextNode = temp.next
        #         temp.next = pre
        #         pre = temp
        #         temp = nextNode
        #     return pre
        # l1 = reverse(l1)
        # l2 = reverse(l2)
        
        # carry = 0
        # head = None
        # p,q= l1,l2
        # while p or q or carry:
        #     x= p.val if p else 0
        #     y= q.val if q else 0
        #     total = x+y+carry
        #     carry = total//10
        #     digit = total%10
            
        #     node = ListNode(digit)
        #     node.next =head
        #     head = node

        #     if p: p =p.next
        #     if q: q= q.next
        
        # return head

        



        