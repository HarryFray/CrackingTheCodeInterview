class Node:
    def __init__(self,inidata):
        self.data = inidata
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def viewlinkedlist(self):
        current = self.head
        while current != None:
            print current.data,
            current = current.next

    def add(self,val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp




LList = LinkedList()
LList.add(1)
LList.add(2)

print LList.viewlinkedlist()







