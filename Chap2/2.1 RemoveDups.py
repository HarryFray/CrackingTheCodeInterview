class Node:
    def __init__(self,inidata):
        self.data = inidata
        self.next = None

''' creates linked list by setting init val as head'''
class LinkedList:
    def __init__(self,init):
        self.head = Node(init)
        self.next = None


    ''' view list for testing'''
    def viewlinkedlist(self):
        current = self.head
        while current != None:
            print current.data,
            current = current.next
    ''' adds new val to front of linked list'''
    def add(self,val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def RemoveDups(self):
        valsinlist = [self.head.data]

        cur = self.head.next
        prev = self.head

        while cur != None:
            valsinlist.append(cur.data)
            print valsinlist
            if prev.data in valsinlist:
                print 'found dup'
                prev = cur
                cur = cur.next
            else:
                print 'no dup found'
                prev = cur
                cur = cur.next
        return valsinlist


LList = LinkedList(8)
LList.add(1)
LList.add(4)
LList.add(3)
LList.add(2)
LList.add(5)
LList.add(9)

#LList.viewlinkedlist()
print LList.RemoveDups()









