class Node:
    def __init__(self, value):
        # node has a value and its next value is always None
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # here using the class to create node
        new_node = Node(value)
        # In linked list there is a head value and a tail value, so we are setting that manually
        self.head = new_node
        self.tail = new_node
        # when the node is added we have to manually adjust the increment in the length
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        # edge case 1: when the list is already empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # edge case 1: when the list is already empty
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            # edge case 2: when there is only one node in the list, means when we pop off one time the head and tail
            # will still points to that node even with length 0, so we are setting both to None
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp

    def prepend(self, value):
        new_node = Node(value)
        # edge case 1: empty list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        # edge case 1: empty list
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        # edge case 2: after decrementing length to 0, the last node is pop but tail was still pointing to it
        if self.length == 0:
            self.tail = None
        return temp


my_list = LinkedList(4)
my_list.append(10)
my_list.append(20)
my_list.print_list()
my_list.pop()
my_list.print_list()
my_list.prepend(120)
my_list.print_list()
