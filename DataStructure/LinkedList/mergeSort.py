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

    

def mergeSort(temp):
    if temp is None or temp.next is None:
        return temp
        
    mid = getMiddle(temp)
    midNext = mid.next
    mid.next = None

    left = mergeSort(temp)
    right = mergeSort(midNext)

    sortedList = mergeList(left,right)
    return sortedList

def getMiddle(node):

    if node is None:
        return node

    slow = node
    fast = node.next

    while(fast != None):
        fast = fast.next

        if (fast != None):
            slow = slow.next
            fast = fast.next
    return slow
        

def mergeList(head1,head2):

    sortedList = LinkedList()

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

ll1.insertAtBegin(20)
ll1.insertAtBegin(15)
ll1.insertAtBegin(10)
ll1.insertAtBegin(25)
ll1.insertAtBegin(-8)
ll1.insertAtBegin(3)
ll1.insertAtBegin(12)
ll1.insertAtBegin(5)
ll1.insertAtBegin(0)
ll1.insertAtBegin(8)
ll1.printLinkedList(ll1)
print()

ll3 = LinkedList()
ll3.head = mergeSort(ll1.head)
ll3.printLinkedList(ll3)
print()



