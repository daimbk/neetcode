class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        # node = [val, pointer]
        self.head = None
        self.tail = None
        self.index = -1
    
    def get(self, index: int) -> int:
        if index > self.index or index < 0:
            return -1

        if index == 0:
            return self.head.val

        if index == self.index:
            return self.tail.val

        node = self.head

        for i in range(index):
            node = node.next

        return node.val

    def insertHead(self, val: int) -> None:
        new_head = Node(val, self.head)
        self.head = new_head
        self.index += 1
        
        if self.tail == None:
            self.tail = self.head

    def insertTail(self, val: int) -> None:
        if self.tail == None:
            self.head = Node(val, None)
            self.tail = self.head
            self.index += 1
            return

        node = Node(val, None)
        self.tail.next = node
        self.tail = node
        self.index += 1

    def remove(self, index: int) -> bool:
        if index > self.index or index < 0:
            return False

        if index == 0:
            self.head = self.head.next
            self.index -= 1
            return True
        
        prev_node = None
        node = self.head
        next_node = None
        for i in range(index):
            prev_node = node
            node = node.next
            next_node = node.next

        prev_node.next = next_node

        if index == self.index:
            self.tail = prev_node

        self.index -= 1
        return True

    def getValues(self) -> List[int]:
        array = []
        node = self.head
        for i in range(self.index + 1):
            array.append(node.val)
            node = node.next

        return array