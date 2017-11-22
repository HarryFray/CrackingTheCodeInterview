from NodePractice import UnorderedList
''' codes idea is correct my add has an issue that prevents this from running correctly 
object has no attribute next? it must because the list addmultiple works with it...'''
def DeleteNode(node):
    node.data = node.next.data # takes data of next node
    node.next = node.next.next # then skips next node



LList = UnorderedList()

LList.AddMultiple([1,6,8,3,0])
midnode = LList.add(2)
LList.AddMultiple([5,4,6,7])

LList.viewlinkedlist()
print ""
DeleteNode(midnode)
print ""
LList.viewlinkedlist()