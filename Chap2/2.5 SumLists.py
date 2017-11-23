from NodePractice import UnorderedList
''' goals: 1. account for linked lists of different length
           2. solve problem when digits are in opposite order
           '''

''' solved with recursion'''
def SumLists(LL1,LL2):
    if LL1 == None:return 0
    else:return LL1.data + LL2.data + SumLists(LL1.next,LL2.next)*10


Alist = UnorderedList()
Alist.AddMultiple([7,1,5])
Blist = UnorderedList()
Blist.AddMultiple([5,9,2])

Alist.viewlinkedlist()
Blist.viewlinkedlist()

print SumLists(Alist.head,Blist.head)

