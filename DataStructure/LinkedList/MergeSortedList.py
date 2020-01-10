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

    def insertAtEnd(self,data):
        newNode = Node(data)
        curr = self.head
        while(curr.next):
            curr = curr.next
        curr.next = newNode
            
    def printLinkedList(self,linkedList):
        curr = self.head
        while(curr):
            print(curr.data, end = " ")
            curr = curr.next

def mergeList(head1,head2):

    sortedList = None

    if head1 is None:
        return head2

    if head2 is None:
        return head1
        
    if head1.data <= head2.data:
        sortedList = head1
        sortedList.next = mergeList(head1.next, head2)
    else:
        sortedList = head2
        sortedList.next = mergeList(head1, head2.next)

    return sortedList
            

ll1 = LinkedList()
ll2 = LinkedList()

ll1.insertAtBegin(20)
ll1.insertAtBegin(15)
ll1.insertAtBegin(10)
ll1.insertAtBegin(5)
ll1.insertAtBegin(0)
ll1.printLinkedList(ll1)
print()

ll2.insertAtBegin(24)
ll2.insertAtBegin(15)
ll2.insertAtBegin(8)
ll2.insertAtBegin(3)
ll2.insertAtBegin(1)
ll2.printLinkedList(ll2)
print()

ll3 = LinkedList()
ll3.head = mergeList(ll1.head,ll2.head)
ll3.printLinkedList(ll3)
print()



