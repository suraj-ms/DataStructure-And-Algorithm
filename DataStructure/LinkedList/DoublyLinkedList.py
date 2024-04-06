class Node:
    def __init__(self, Value):
        self.value = Value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)
    
class DublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1       

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        if self.head is None:
            return None
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next
    
    def reverseTraverse(self):
        if self.head is None:
            return None
        current_node = self.tail
        while current_node:
            print(current_node)
            current_node = current_node.prev
    
    def search(self, target):
        if self.head is None:
            return None
        else:
            current_node = self.head
            index = 0
            while current_node:
                if(current_node.value == target):
                    return index
                current_node = current_node.next
                index += 1
            return -1
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length-1,index,-1):
                current_node = current_node.prev
        return current_node
    
    def Update(self, index, value):
        if index < 0 or index >= self.length:
            return None
        update_node = self.get(index)
        if update_node:
            update_node.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            print("index out of range")
            return 
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        else:
            temp_node = self.get(index-1)
            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next.prev = new_node
            temp_node.next = new_node
        self.length += 1

    def popFirst(self):
        pop_node = self.head
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            pop_node.next = None
        self.length -= 1
        return pop_node
    
    def pop(self):
        pop_node = self.tail
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.tail = self.tail.prev
            self.tail.next = None
            pop_node.next = None
        self.length -= 1
        return pop_node

    def remove(self, index):
        if self.head is None:
            return None
        elif index < 0 or index >= self.length:
            print("index out of range")
            return 
        elif index == 0:
            pop_node = self.popFirst()
            return pop_node
        elif index == self.length-1:
            pop_node = self.pop()
            return pop_node
        else:
            pop_node = self.get(index)
            pop_node.prev.next = pop_node.next
            pop_node.next.prev = pop_node.prev
            pop_node.prev = None
            pop_node.next = None
        self.length -= 1
        return pop_node 
    
    def clear(self):
        self.head = None
        self.tail = None
        print("Done...")



dll = DublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(50)
dll.prepend(60)
# dll.append(50)
# dll.prepend(60)
# dll.append(70)
# dll.append(80)
# dll.prepend(90)
print(dll)
# print(dll.insert(6,90))
print(dll.clear())
print(dll)
# dll.reverseTraverse()