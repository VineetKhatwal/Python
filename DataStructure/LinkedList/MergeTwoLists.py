class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

            
    def printLinkedList(self,linkedList):
        curr = self.head
        while(curr):
            print(curr.data, end = " ")
            curr = curr.next

def sort(ll1, ll2):
    sortedList = None
        
    if not ll1:
        return ll2
        
    if not ll2:
        return ll1
        	
    if ll1.data < ll2.data:
        sortedList.data = ll1.data
        sortedList.next = sort(ll1.next, ll2)
    else:
        sortedList.data = ll2.data
        sortedList.next = sort(ll1, ll2.next)
        
    return sortedList 
            

ll1 = LinkedList()
ll1.insertAtBegin(2)
ll1.insertAtBegin(10)
ll1.insertAtBegin(14)

ll2 = LinkedList()
ll2.insertAtBegin(2)
ll2.insertAtBegin(3)
ll2.insertAtBegin(18)
print()

ll3 = LinkedList()
ll3.head = sort(ll1.head,ll2.head)
ll3.printCircularLinkedList(ll3)
