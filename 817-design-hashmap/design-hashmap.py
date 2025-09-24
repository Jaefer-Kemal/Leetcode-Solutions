class Node:
    def __init__(self, key = -1, value = -1):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def appendOrUpdate(self, key, value):
        new_node = Node(key,value)
        if (not self.head):
            self.head =  new_node
            return 
        
        curr = self.head
        while curr.next:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        if curr.key == key:
            curr.value = value
            return
        curr.next = new_node
     
    def delete(self, key):
        curr = self.head
        if curr and curr.key == key:
            self.head = curr.next
            return
        
        prev = None
        while curr and curr.key != key:
            prev = curr
            curr = curr.next
        
        if curr:
            value = curr.value
            prev.next = curr.next
    
    
    def display(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        
        return -1


class MyHashMap:
    def __init__(self):
        self.hashMap = [LinkedList() for _ in range(1000)]
    
    def _hash(self, key: int) -> int:
        return key % 1000

    def put(self, key: int, value: int) -> None:
        nodes = self.hashMap[self._hash(key)]
        nodes.appendOrUpdate(key, value)
        

    def get(self, key: int) -> int:
        nodes = self.hashMap[self._hash(key)]
        return nodes.display(key)
        

    def remove(self, key: int) -> None:
        nodes = self.hashMap[self._hash(key)]
        nodes.delete(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)