
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
        else:
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

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        if self.head is None:
            return None

        if self.head.next is None:
            return self.head

        while fast:
            if fast.next is None:
                return slow
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self):
        slow = self.head 
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
    
    def remove_duplicates(self):
        if self.head is None:
            return None
        
        temp = self.head
        prev = None
        seen = set()
      
        while temp:
            if temp.value in seen:
                prev.next = temp.next
                self.length -= 1
            else:
                seen.add(temp.value)
                prev = temp
            temp = temp.next

    def binary_to_decimal(self):

        current_node = self.head
        current_value = 0

        while current_node:
            current_value = (current_value * 2) + current_node.value
            current_node = current_node.next

        return current_value

    def partition_list(self, x):
        d1 = NewNode(0)
        d2 = NewNode(0)

        prev1 = d1
        prev2 = d2

        if self.head is None:
            return None

        current = self.head

        for _ in range(self.length):
            if current.value < x:
                prev1.next = current
                prev1 = prev1.next

            if current.value >= x:
                prev2.next = current
                prev2 = prev2.next
            current = current.next

        prev2.next = None
        prev1.next = d2.next
        self.head = d1.next

        return True

    def reverse_between(self, start_index, end_index):
        dummy = NewNode(0)
        dh = dummy
        current_dummy = dummy
        current = self.head

        p1 = current
        p2 = current

        target_index_1 = start_index 
        target_index_2 = end_index 

        for i in range(self.length):
            if target_index_1 == i:

                p1 = current
                current_dummy = current.next
                dh.next = current_dummy
                current_dummy.next = current.next
                
                
            if target_index_2 == i:
                p2 = current

            if current.value > start_index and current.value <= end_index:
    
                print(current_dummy.value)
            current = current.next
        
        # while dh:
        #     # print(dh.value)
        #     dh = dh.next
        p1.next = dh
        # dh.next = None
        current_dummy.next = p2
        return True


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

myList = LinkedList(0)
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(6)

myList.append(7)
myList.append(8)




myList.reverse_between(2,4)
myList.print_list()




            #     print(d1.value)

        # target_index_2 = end_index -1

            #     current_dummy = current_dummy.next
            #     dt = current_dummy
            #     print("current_dummy", current_dummy.value)
              
            # current = current.next
            # current_dummy.next = None
            # current_dummy.next = p2


