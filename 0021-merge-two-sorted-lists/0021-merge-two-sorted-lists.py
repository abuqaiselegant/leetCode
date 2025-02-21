# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        temp1 = list1
        temp2 = list2
        while temp1 is not None and temp2 is not None:
            if temp1.val <= temp2.val:
                a.append(temp1.val)
                temp1 = temp1.next
            # elif temp1.val < temp2.val:
            #     a.append(temp1.val)
            #     temp1 = temp1.next
            else:
                a.append(temp2.val)
                temp2 = temp2.next
        while temp1 is not None:
            a.append(temp1.val)
            temp1 = temp1.next
        while temp2 is not None:
            a.append(temp2.val)
            temp2 = temp2.next
        
        if not a :
            return None

        newNode = ListNode(a[0])
        current = newNode
        for i in range(1,len(a)):
            current.next = ListNode(a[i])
            current = current.next
        return newNode

# #second method
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         NewNode = ListNode()
#         temp = NewNode

#         while list1 is not None and list2 is not None:
#             if list1.val <= list2.val:
#                 temp.next = list1
#                 list1 = list1.next
#             else:
#                 temp.next = list2
#                 list2 = list2.next
#             temp = temp.next
        
#         if list1 is not None:
#             temp.next = list1
#         elif list2 is not None:
#             temp.next = list2
        
#         return NewNode.next