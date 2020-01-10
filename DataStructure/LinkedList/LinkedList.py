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
            
    def deleteAtBegin(self):
        self.head = self.head.next

    def deleteAtEnd(self):
        curr = self.head
        prev = None
        while(curr.next):
            prev = curr
            curr = curr.next
        prev.next = curr.next

    def insertElementBefore(self,target,data):
        newNode = Node(data)

        curr = self.head
        prev = None

        if curr.data == target:
            #insertAtBegin(data)
            newNode.next = self.head
            self.head = newNode
            return

        while (curr and curr.data != target):
            prev = curr
            curr = curr.next
            
        if curr is not None:
            if prev:
                prev.next = newNode
            newNode.next = curr
            return
        else:
            print("Element",target,"not found in the list")

    def deleteElement(self,target):

        curr = self.head
        prev = None

        if curr.data == target:
            self.head = self.head.next
            return

        while (curr and curr.data != target):
            prev = curr
            curr = curr.next
            
        if curr is not None:
            prev.next = curr.next
            return
        else:
            print("Element",target,"not found in the list")

    def insertAtPosition(self,pos,data):
        newNode = Node(data)

        curr = self.head
        prev = None

        if pos == 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        counter = 0
        
        while (curr):
            if (counter == pos):
                if prev:
                    prev.next = newNode
                newNode.next = curr
                break
            else:
                prev = curr
                curr = curr.next
                counter += 1
            
        if curr is None:
            print("Position",pos, "is out of index in the linked list")

    def deleteAtPosition(self,pos):

        curr = self.head
        prev = None

        if pos == 0:
            self.head = self.head.next
            return
        
        counter = 0
        
        while (curr):
            if (counter == pos):
                prev.next = curr.next
                break
            else:
                prev = curr
                curr = curr.next
                counter += 1
            
        if curr is None:
            print("Position",pos, "is out of index in the linked list")
            

    def printLinkedList(self,linkedList):
        curr = self.head
        while(curr):
            print(curr.data, end = " ")
            curr = curr.next
            

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

ll.deleteAtBegin()
ll.deleteAtEnd()
ll.printLinkedList(ll)
print()

ll.insertElementBefore(5,0)
ll.insertElementBefore(15,14)
ll.insertElementBefore(30,28)
ll.insertElementBefore(10,8)
ll.printLinkedList(ll)
print()

ll.insertAtPosition(0,-5)
ll.insertAtPosition(5,12)
ll.insertAtPosition(11,35)
ll.insertAtPosition(14,35)
ll.printLinkedList(ll)
print()

ll.deleteElement(8)
ll.deleteElement(35)
ll.deleteElement(30)
ll.deleteElement(-5)
ll.deleteElement(5)
ll.printLinkedList(ll)
print()

ll.deleteAtPosition(0)
ll.printLinkedList(ll)
print()

ll.deleteAtPosition(7)
ll.printLinkedList(ll)
print()


ll.deleteAtPosition(6)
ll.printLinkedList(ll)
print()

ll.deleteAtPosition(2)
ll.printLinkedList(ll)
print()


            

        
         
            

        

        
    
