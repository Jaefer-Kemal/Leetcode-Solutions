class Node:
    def __init__(self, val = -1):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.k = k
        self.length = 0

    def insertFront(self, value: int) -> bool:
        if self.length == self.k:
            return False
        
        new_node = Node(value)

        next_node = self.head.next

        self.head.next = new_node
        next_node.prev = new_node

        new_node.next = next_node
        new_node.prev = self.head

        self.length += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.length == self.k:
            return False

        new_node = Node(value)

        previous_node = self.tail.prev

        previous_node.next = new_node
        self.tail.prev = new_node

        new_node.next = self.tail
        new_node.prev = previous_node
        
        self.length += 1

        return True
    def deleteFront(self) -> bool:
        if self.length == 0:
            return False

        self.head.next = self.head.next.next

        self.head.next.prev = self.head

        self.length -= 1

        return True

    def deleteLast(self) -> bool:
        if self.length == 0:
            return False
        
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        self.length -= 1

        return True
        

    def getFront(self) -> int:
        return self.head.next.val
        

    def getRear(self) -> int:
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()