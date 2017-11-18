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

class RandomList:
    def __init__(self,init_node):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head # pointing added node to previouse head node
        self.head = temp # assigning your new node to the head of the list

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count


LList = RandomList(22)

LList.add(24)
LList.add(12)
LList.add(21)

print RandomList.length(LList)
