#   Created by Elshad Karimov on 01/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value) 

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # def __iter__(self):
    #     node = self.head
    #     while node:
    #         yield node
    #         node = node.next
    #         if node == self.tail.next:
    #             break
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result
    
    def appendCSLL(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def prependCSLL(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
    
    def insertInCSLL(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            print("Index out of range")
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
    
    def traverseCSLL(self):
        if self.head is None:
            print("List is empty")
            return False
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
    
    def searchInCSLL(self, target):
        if self.head is None:
            print("List is empty")
            return -1
        index = 0
        temp_node = self.head
        while temp_node.value != target:
            temp_node = temp_node.next
            index += 1
        print(f"Value is present in index {index}")

    def get(self, value):
        if self.head is None:
            print("List is empty")
            return None
        elif value == -1:
            return self.tail
        elif value < -1 or value > self.length:
            print("Index out of range")
            return None
        temp_node = self.head
        for _ in range(value):
            temp_node = temp_node.next
        return temp_node

    def UpdateCSLL(self, index, value):
        temp_node = self.get(index)
        print(temp_node)
        if temp_node:
            temp_node.value = value
            return True
        return False
    
    def popFirst(self):
        pop_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            pop_node.next = None
        self.length -= 1
        return pop_node
    
    def pop(self):
        if self.head is None:
            return None
        pop_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else: 
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            pop_node    .next = None
            self.tail = temp
        self.length -= 1
        return pop_node
    
    def remove(self, index):
        if self.head is None:
            return None
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == -1 or index == self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
        
    
    def clear(self):
        self.head = None
        self.tail = None
        print("Done...")

    

circularSLL = CircularSinglyLinkedList()
circularSLL.appendCSLL(10)
circularSLL.appendCSLL(20)
# print(circularSLL)
circularSLL.prependCSLL(30)
# print(circularSLL)
circularSLL.insertInCSLL(1,60)
# print(circularSLL)
# circularSLL.insertInCSLL(-10,50)
# print(circularSLL)
# circularSLL.traverseCSLL()
# circularSLL.clear()
# print(circularSLL.UpdateCSLL(0,90))
print(circularSLL.remove(2))
print(circularSLL)













