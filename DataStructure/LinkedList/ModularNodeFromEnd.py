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

    def getLength(self):
        curr = self.head
        length = 0
        while(curr):
            length += 1
            curr = curr.next
        return length

    def printModularNode(self, n):
        length = self.getLength()
        while (length % n != 0):
            length -= 1

        counter = 1
        curr = self.head
        print()

        while(curr):
            if counter == length:
                print("Breaking", curr.data)
                break

            curr = curr.next
            counter += 1


ll = LinkedList()
ll.insertAtBegin(30)
ll.insertAtBegin(25)
ll.insertAtBegin(20)
ll.insertAtBegin(15)
ll.insertAtBegin(10)
ll.insertAtBegin(5)
ll.insertAtBegin(0)
ll.printLinkedList(ll)

ll.printModularNode(1)
ll.printModularNode(2)
ll.printModularNode(3)
ll.printModularNode(4)
ll.printModularNode(5)
ll.printModularNode(6)
ll.printModularNode(7)
print()
