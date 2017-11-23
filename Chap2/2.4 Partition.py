from NodePractice import UnorderedList

''' code works however it would be shorter with a doubly linked list'''
def Partition(LList,split):
    cur = LList.head.next
    for ii in range(LList.length()-1):
        if cur.data >= split:
            LList.append(cur.data)
            cur.data = cur.next.data # assigns cur to next node.data
            cur.next = cur.next.next # points cur around copied node
        else:
            cur = cur.next
    return LList.viewlinkedlist()
 
LList = UnorderedList()
LList.AddMultiple([9,6,8,9,0,0,2,5,8,3,0,7,9,1])
LList.viewlinkedlist()
print ''
print Partition(LList,5)
