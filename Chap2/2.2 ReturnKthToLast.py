from NodePractice import UnorderedList

''' works however far better method for solving using runner ahead of current'''
def ReturnKth(LList,k):
    cur = LList.head
    List = []
    while cur.next != None:
        List.append(cur.data)
        cur = cur.next # can iterate through the rest of list because first cur was set to
    return List[-k+1]

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
print ReturnKth(LList,3)

