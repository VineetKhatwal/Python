class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CicrularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAtBegin(self,data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head
            

    def insertAtEnd(self,data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
            
    def deleteAtBegin(self):

        self.head = self.head.next
        self.tail.next = self.head
        
    def deleteAtEnd(self):
        curr = self.head
        prev = None
        while(curr.next != self.head):
            prev = curr
            curr = curr.next
        self.tail = prev
        self.tail.next = self.head

    def insertElementBefore(self,ll,target,data):
        newNode = Node(data)

        curr = self.head
        prev = None

        if curr.data == target:
            ll.insertAtBegin(data)
            return

        while (curr.data != target):
            prev = curr
            curr = curr.next
            if (curr.data == self.head.data):
                break
            
        if curr != self.head:
            if prev:
                prev.next = newNode
            newNode.next = curr
            return
        else:
            print("Element",target,"not found in the list")

    def deleteElement(self,ll,target):

        curr = self.head
        prev = None

        if curr.data == target:
            ll.deleteAtBegin()
            return

        while (curr.data != target):
            prev = curr
            curr = curr.next
            if (curr.data == self.head.data):
                break
            
        if curr != self.head:
            prev.next = curr.next
            return
        else:
            print("Element",target,"not found in the list")

    def insertAtPosition(self,ll,pos,data):
        newNode = Node(data)

        curr = self.head
        prev = None

        if pos == 0:
            ll.insertAtBegin(data)
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
                if (curr == self.head):
                    break

            
        if curr == self.head:
            print("Position",pos, "is out of index in the linked list")

    def deleteAtPosition(self,pos):

        curr = self.head
        prev = None

        if pos == 0:
            ll.deleteAtBegin()
            return
        
        counter = 0
        
        while (curr):
            if (counter == pos):
                #print("Data " , prev.data, curr.data, curr.next.data)
                prev.next = curr.next
                break
            else:
                prev = curr
                curr = curr.next
                counter += 1
                if (curr == self.head):
                    break
            
        if curr == self.head:
            print("Position",pos, "is out of index in the linked list")
            

    def printLinkedList(self,linkedList):
        curr = self.head
        while(curr):
            print(curr.data, end = " ")
            curr = curr.next
            if (curr == self.head): 
                break 

            

ll = CicrularLinkedList()

ll.insertAtBegin(20)
ll.insertAtBegin(15)
ll.insertAtBegin(10)
ll.insertAtBegin(5)
ll.insertAtBegin(0)
ll.printLinkedList(ll)
print()
ll.insertAtEnd(25)
ll.insertAtEnd(30)
ll.insertAtEnd(35)
ll.printLinkedList(ll)
print()


ll.deleteAtBegin()
ll.printLinkedList(ll)
print()

ll.deleteAtEnd()
ll.printLinkedList(ll)
print()

ll.insertElementBefore(ll,5,0)
ll.insertElementBefore(ll,10,8)
ll.insertElementBefore(ll,15,14)
ll.insertElementBefore(ll,30,28)
ll.insertElementBefore(ll,35,28)
ll.printLinkedList(ll)
print()


ll.insertAtPosition(ll,0,-5)
ll.insertAtPosition(ll,5,12)
ll.insertAtPosition(ll,12,35)
ll.insertAtPosition(ll,11,27)
ll.insertAtPosition(ll,14,35)
ll.printLinkedList(ll)
print()


ll.deleteElement(ll,-5)
ll.printLinkedList(ll)
print()

ll.deleteElement(ll,8)
ll.printLinkedList(ll)
print()

ll.deleteElement(ll,35)

ll.printLinkedList(ll)
print()

ll.deleteElement(ll,30)
ll.deleteElement(ll,5)
ll.printLinkedList(ll)
print()


print("======== Deleting at Position =========")
ll.deleteAtPosition(0)
ll.printLinkedList(ll)
print()

ll.deleteAtBegin()
ll.printLinkedList(ll)
print()

ll.deleteAtPosition(0)
ll.printLinkedList(ll)
print()

ll.deleteAtPosition(8)
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

       

        
         
            

        

        
    
