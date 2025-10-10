class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def add_item(self, val):
        new_node = Node(val)
        if not self.head.next:
            self.head.next = new_node
            return True

        isNotPresent = True
        curr = self.head
        while curr.next:
            if curr.val == val:
                isNotPresent = False
            curr = curr.next

        if curr.val == val:
            isNotPresent = False    
        curr.next = new_node

        return isNotPresent
    
    def remove_item(self, val):
        if not self.head.next:
            return False
        
        curr = self.head.next
        prev = self.head

        while curr.next:
            if curr.val == val:
                prev.next = curr.next
                return True

            prev = prev.next
            curr = curr.next
        
        if curr.val == val:
            prev.next = curr.next
            return True
        
        return False
        
class RandomizedCollection:

    def __init__(self):
        self.multiset = [LinkedList() for _ in range(100000)]
        self.values = []

    def _hash(self, key):
        return key % 100000
        
    def insert(self, val: int) -> bool:
        key = self._hash(abs(val))
        self.values.append(val)
        return self.multiset[key].add_item(val)

    def remove(self, val: int) -> bool:
        key = self._hash(abs(val))
        index_to_remove = -1
        for i, value in enumerate(self.values):
            if val == value:
                index_to_remove = i
                break
            
        if index_to_remove != -1:
            self.values[-1], self.values[index_to_remove] =  self.values[index_to_remove], self.values[-1]
            self.values.pop()

        return self.multiset[key].remove_item(val)

    def getRandom(self) -> int:
        return random.choice(self.values)

        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()