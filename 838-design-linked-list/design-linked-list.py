class Node:

    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.length = 0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        half = index // 2

        if index < half:
            curr = self.head
            position = 0
            while curr:
                if position == index:
                    return curr.next.val
                
                curr = curr.next
                position += 1
        else:
            curr = self.tail
            position = self.length - 1

            while curr:
                if position == index:
                    return curr.prev.val
                
                position -= 1
                curr = curr.prev

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        next_node = self.head.next

        new_node.next = next_node
        new_node.prev = self.head

        self.head.next = new_node
        next_node.prev = new_node

        self.length += 1

        return
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        previous_node = self.tail.prev

        new_node.next = self.tail
        new_node.prev = previous_node

        self.tail.prev = new_node
        previous_node.next = new_node

        self.length += 1

        return
    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0 or index > self.length:
            return 
        
        
        new_node = Node(val)

        position = 0
        curr = self.head

        while curr:
            if position == index:
                previous_node = curr
                next_node = curr.next

                new_node.next = next_node
                new_node.prev = previous_node

                next_node.prev = new_node
                previous_node.next = new_node

                self.length += 1
                return
            
            position += 1
            curr = curr.next


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        
        position = 0
        curr = self.head

        while curr:
            if position == index:
                previous_node = curr
                next_node = curr.next.next

                previous_node.next = next_node
                next_node.prev = previous_node

                self.length -= 1
                return

            position += 1
            curr = curr.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)