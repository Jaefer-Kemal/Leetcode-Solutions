class Node:
    def __init__(self, val = None, index = -1):
        self.value = val
        self.index = index
        self.next = None
        self.prev = None
        

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node()
        self.tail = Node()
        
        home_node = Node(homepage,1)

        self.head.next = home_node
        home_node.next = self.tail

        self.tail.prev = home_node
        home_node.prev = self.head

        self.length = 1
        self.current_page = home_node

    def visit(self, url: str) -> None:
        index = self.current_page.index
        self.length = index + 1

        url_node = Node(url, self.length)

        self.current_page.next = url_node
        url_node.prev = self.current_page

        url_node.next = self.tail
        self.tail.prev = url_node

        self.current_page = url_node

    def back(self, steps: int) -> str:
        index = self.current_page.index

        if steps >= index:
            self.current_page = self.head.next
            return self.current_page.value
        
        for _ in range(steps):
            self.current_page = self.current_page.prev

        return self.current_page.value

    def forward(self, steps: int) -> str:
        index = self.current_page.index

        if index + steps > self.length:
            self.current_page = self.tail.prev
            return self.current_page.value

        for _ in range(steps):
            self.current_page = self.current_page.next
        
        return self.current_page.value
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)