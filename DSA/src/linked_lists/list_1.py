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

    def pop(self):
        current_node = self.head.next
        next_node = current_node.next
        if current_node is None:
            return None

        while current_node:
            print("current", current_node.data)
            print("next", next_node)
            if next_node.next is None:
                print("loop")
                current_node.next = None
                self.tail = current_node
                break
            current_node = next_node
            next_node = current_node.next
            print("end")

        return None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


myList = Linked_List(0)
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.pop()

myList.print_list()