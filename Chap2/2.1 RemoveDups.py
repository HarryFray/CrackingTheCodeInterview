from NodePractice import UnorderedList


''' remove duplicates works but uses a buffer 
        should try using a prev and cur to avoid this 
        also what am I  passing here? a linked list should be 
        the input'''

def RemoveDups(linkedlist):
    cur = linkedlist.head
    setting = set([cur.data])
    while cur.next:
        if cur.next.data in setting:
            cur.next = cur.next.next
        else:
            setting.add(cur.next.data)
            cur = cur.next
    return LList.viewlinkedlist()



LList = UnorderedList()
LList.add(7)
LList.add(2)
LList.add(1)
LList.add(9)
LList.add(9)
LList.add(2)
LList.add(5)
LList.add(2)
LList.add(2)

#LList.viewlinkedlist()
print RemoveDups(LList)










