class NewNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
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



    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


myList = LinkedList(1)
myList.append(2)
myList.prepend(10)

myList.print_list()
