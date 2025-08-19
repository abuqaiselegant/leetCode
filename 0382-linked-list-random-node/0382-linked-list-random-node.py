# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        temp = self.head
        self.count = 0
        while temp:
            self.count +=1
            temp = temp.next

    def getRandom(self) -> int:
        index = random.randint(0, self.count-1)
        temp = self.head
        x = 0
        while temp:
            if index == x:
                return temp.val
            temp = temp.next
            x+=1
            

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()