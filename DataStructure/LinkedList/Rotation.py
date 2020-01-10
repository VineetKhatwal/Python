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

    def linkedListReverser(self):

        curr = self.head
        prev = None
        next = None

        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def linkedListRotator(self, ll, direction, n):

        if direction == "left":
            ll.linkedListReverser()

        count = 1
        curr = self.head
        while (count < n):
            curr = curr.next
            count += 1
            
        temp = curr.next
        curr.next = None

        curr = temp

        while(curr.next):
            curr = curr.next

        curr.next = self.head
        self.head = temp

        if direction == "left":
            ll.linkedListReverser()
        
        return
    
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

ll.linkedListRotator(ll,"left",3 )
ll.printLinkedList(ll)
print()

