from DoubleLinkedList import DoubleList
''' works using double linked lists...
try and solve recursively next time'''
def Palindrome(LList):
    beg = LList.head
    end = LList.tail
    for ii in range(linked.LLLength()/2):
        if beg.data == end.data:
            beg = beg.next
            end = end.prev
        else:
            return False
    return True


linked = DoubleList()
linked.appendmore([1,2,3,4,4,3,2,1])
linked.viewlinkedlist()
print Palindrome(linked)







