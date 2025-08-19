class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        temp = self.head
        while temp:
            if count == index:
                return temp.val
            temp = temp.next
            count +=1
        return -1

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        temp.next = self.head
        self.head = temp


    def addAtTail(self, val: int) -> None:
        temp = self.head
        tail = Node(val)
        if temp is None:
            self.head = tail
            return
        while temp.next:
            temp = temp.next
        temp.next = tail

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        if index ==0:
            newNode.next = self.head
            self.head = newNode
            return 
        temp = self.head
        count = 0
        while temp and count<index-1:
            temp = temp.next
            count+=1
        if temp is None:
            return 
        newNode.next =temp.next
        temp.next = newNode

        

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return
        if index == 0:
            self.head = self.head.next
            return 
        temp = self.head
        count = 0
        while temp and count <index-1:
            temp= temp.next
            count+=1
        if temp is None or temp.next is None:
            return
        temp.next = temp.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)