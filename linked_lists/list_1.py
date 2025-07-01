
"""    
    This module implements a singly linked list data structure with basic operations.

    Classes:
        NewNode:
            Represents a node in a singly linked list, storing a value and a reference
            to the next node.

        LinkedList:
            Implements a singly linked list supporting the following operations:
                - append(value): Add a node with the given value to the end of the list.
                - pop(): Remove and return the last node from the list.
                - prepend(value): Add a node with the given value to the beginning of the list.
                - pop_first(): Remove and return the first node from the list.
                - get(index): Retrieve the node at the specified index.
                - set(index, value): Update the value of the node at the specified index.
                - print_list(): Print all values in the list.
"""

class NewNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0
        if value is not None:
            new_node = NewNode(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1


    def append(self, value):
        new_node = NewNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

        return True


    def pop(self):
        current_node = self.head
        previous_node = self.head

        if self.length == 0:
            return None

        while current_node.next:
            previous_node = current_node
            current_node = current_node.next

        self.tail = previous_node
        self.tail.next = None
        self.length -=1

        if self.length == 0:
            self.head = None
            self.tail = None

        return current_node

    def prepend(self, value):
        new_node = NewNode(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range (index):
            temp = temp.next
        return temp


    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
  
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = NewNode(value)
        temp = self.get(index - 1)
        if temp:
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None
        self.length -= 1

        return temp



    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


myList = LinkedList(0)
myList.append(1)
myList.append(2)
myList.append(3)

myList.remove(3)

myList.print_list()
