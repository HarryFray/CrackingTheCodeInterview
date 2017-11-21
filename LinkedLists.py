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




linkedlist = linked_list() #creates empty list

linkedlist.head = Node(1) #creates first node (head node)
sec = Node(2) # creates second node ect.
thrd = Node(2)
frth = Node(5)

# pointers from one node to another
linkedlist.head.next = sec
sec.next = thrd
thrd.next = frth

linkedlist += 

linkedlist.printList()







