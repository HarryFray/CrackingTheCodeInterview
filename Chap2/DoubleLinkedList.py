class Node(object):
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleList(object):
    def __init__(self,h = None,t = None):
        self.head = h
        self.tail = t

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def appendmore(self,list):
        for ii in list:
            self.append(ii)


    def viewlinkedlist(self):
        current = self.head
        while current != None:
            print current.data,
            current = current.next
        print ''

    def LLLength(self):
        count = 1
        cur = self.head
        while cur.next:
            cur = cur.next
            count += 1
        return count



