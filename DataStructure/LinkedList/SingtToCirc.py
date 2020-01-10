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

    def printCircularLinkedList(self,linkedList):
        curr = self.head
        while(curr):
            print(curr.data, end = " ")
            curr = curr.next
            if(curr == self.head):
                break

    def singToCirc(self):
        curr = self.head
        while(self.head.next):
            self.head = self.head.next
        self.head.next = curr
        self.head = curr
            

ll = LinkedList()

ll.insertAtBegin(20)
ll.insertAtBegin(15)
ll.insertAtBegin(10)
ll.insertAtBegin(5)
ll.insertAtBegin(0)

ll.insertAtEnd(25)
ll.insertAtEnd(30)
ll.insertAtEnd(35)
ll.printLinkedList(ll)
print()

ll.singToCirc()
ll.printCircularLinkedList(ll)
