class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    '''adds item to front of the list'''
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head) # pointing added node to previouse head node
        self.head = temp # assigning your new node to the head of the list

    '''returns length of passed list'''
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    '''finds location of item'''
    def search(self,item):
        current = self.head
        found = False
        count = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                count += 1
        return found, count

    ''' removes item from list'''
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while found:
            if current.data == item: # stops loop when current == item
                found = True
            else:
                previouse = current
                current = current.next
        # special case where item we want to remove is the first
        if previous == None:
            self.head = current.next

        else:
            previous.next = current.next

    ''' prints list for user'''
    def viewlinkedlist(self):
        current = self.head
        while current != None:
            print current.data,
            current = current.next

    ''' appends item to end of list'''
    def append(self,item):
        newnode = Node(item)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newnode
    ''' returns final value from list assigns it to passed variable '''
    def pop(self):
        current = self.head
        previouse = None
        while current.next != None:
            previouse = current
            current = current.next
        previouse.next = None
        return current.data


    def index(self,index):
        current = self.head
        count = 0
        while count < index:
            current = current.next
            count += 1
        return current.data

mylist = UnorderedList()
# single direction linked list are like stacks
mylist.add(24) # last item in linked list (first added)
mylist.add(12)
mylist.add(2)
mylist.add(4)
mylist.add(16) # first item in linked list (last added)
mylist.append(5)
mylist.append(8)

# print UnorderedList.length(mylist)
#print mylist.search(16)
#mylist.remove(2)
#print UnorderedList.length(mylist)
print mylist.viewlinkedlist()
print mylist.pop()
# print mylist.index(5)
