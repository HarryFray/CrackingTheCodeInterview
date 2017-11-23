class Node:
    def __init__(self,data):
        self.data = data # assign data point
        self.next = None # stores pointer to next node self is the
                         # node and None is what you are pointing to!

class linked_list:
    # creates a linked list
    def __init__(self):
        self.head = Node(data = None)

    def append(self,data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node



    # displays linked list so i can learn this this :)
    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next








