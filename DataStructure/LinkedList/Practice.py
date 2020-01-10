class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self, ll):
        curr = self.head
        while(curr):
            print(curr.data, end=" ")
            curr = curr.next

    def insertAtBegin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        curr = self.head
        while(curr.next):
            #print(curr.data, curr.next.data)
            curr = curr.next
            # print(curr.data)
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

    def insertElementBefore(self, target, data):
        newNode = Node(data)
        curr = self.head
        prev = None

        if curr.data == target:
            newNode.next = self.head
            self.head = newNode
            return

        while(curr and curr.data != target):
            prev = curr
            curr = curr.next

        if (curr):
            prev.next = newNode
            newNode.next = curr
            return
        else:
            print("Element", target, "not found in the list")

    def deleteElement(self, target):
        curr = self.head
        prev = None

        if curr.data == target:
            self.head = self.head.next
            return

        while(curr and curr.data != target):
            prev = curr
            curr = curr.next

        if (curr):
            prev.next = curr.next
            return
        else:
            print("Element", target, "not found in the list")

    def listReversal(self):
        curr = self.head

        prev = None
        next = None

        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

    def listRotator(self, ll, direction, num):

        if direction == "left":
            ll.listReversal()

        curr = self.head
        counter = 1
        while (counter < num):
            curr = curr.next
            counter += 1

        temp = curr.next
        curr.next = None
        curr = temp

        while(curr.next):
            curr = curr.next

        curr.next = self.head
        self.head = temp

        if direction == "left":
            ll.listReversal()

    def returnNthElementFromLast(self, elementNo):

        lenLL = self.head
        curr = self.head
        length = 0

        while(lenLL):
            lenLL = lenLL.next
            length += 1

        temp = length - elementNo
        counter = 0

        if (elementNo > length):
            print("Invalid Number to be returned")
            return

        if (elementNo == length):
            print(curr.data)
            return

        while (curr.next):
            curr = curr.next
            counter += 1
            if counter == temp:
                print(curr.data)

    def removeNthElementFromLast(self, elementNo):

        lenLL = self.head
        curr = self.head
        prev = self.head
        length = 0

        while(lenLL):
            lenLL = lenLL.next
            length += 1

        if (elementNo > length):
            print("Invalid Number")
            return

        if (elementNo == length):
            self.head = self.head.next
            return

        counter = 0
        while (counter < elementNo):
            curr = curr.next
            counter += 1

        while(curr.next):
            curr = curr.next
            prev = prev.next

        prev.next = prev.next.next


ll = LinkedList()

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
ll.insertAtEnd(40)
ll.insertAtEnd(45)
ll.printLinkedList(ll)
print()

ll.deleteAtBegin()
ll.printLinkedList(ll)
print()

ll.deleteAtEnd()
ll.deleteAtEnd()
ll.printLinkedList(ll)
print()

ll.insertElementBefore(5, 0)
ll.insertElementBefore(5, 2)
ll.insertElementBefore(20, 18)
ll.insertElementBefore(35, 33)
ll.insertElementBefore(40, 41)
ll.printLinkedList(ll)
print()

ll.deleteElement(0)
ll.deleteElement(18)
ll.deleteElement(35)
ll.deleteElement(50)
ll.printLinkedList(ll)
print()

print("REVERSING THE LINKED LIST")
ll.listReversal()
ll.printLinkedList(ll)
print()

ll.listReversal()
ll.printLinkedList(ll)
print()

print("ROTATING THE LINKED LIST")
ll.listRotator(ll, "right", 4)
ll.printLinkedList(ll)
print()
ll.listRotator(ll, "left", 4)
ll.printLinkedList(ll)
print()

ll.returnNthElementFromLast(0)
ll.returnNthElementFromLast(1)
ll.returnNthElementFromLast(2)
ll.returnNthElementFromLast(3)
ll.returnNthElementFromLast(4)
ll.returnNthElementFromLast(5)
ll.returnNthElementFromLast(6)
ll.returnNthElementFromLast(7)
ll.returnNthElementFromLast(8)
ll.returnNthElementFromLast(9)
print()
ll.printLinkedList(ll)
print()
ll.removeNthElementFromLast(8)
ll.printLinkedList(ll)
print()
