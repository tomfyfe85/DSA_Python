class New_Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self, value):
        new_node = New_Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = New_Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


myList = Linked_List(4)
myList.append(5)
myList.print_list()