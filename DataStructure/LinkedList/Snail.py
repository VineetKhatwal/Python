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

    def detectSnail(self,ll):
        slow = self.head
        fast = self.head

        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                print("Snail Detected",slow.data, fast.data)
                ll.removeLoop(slow)
                break
            
    def removeLoop(self, slow):
        ptr1 = None
        ptr2 = None

        ptr1 = self.head
    
        while(True):
            ptr2 = slow
            print("0",ptr1.data, ptr2.data)

            while (ptr2.next != slow and ptr2.next != ptr1):
                ptr2 = ptr2.next
                print("1",ptr1.data, ptr2.data)

            if (ptr2.next == ptr1):
                print("2",ptr2.data, ptr2.next.data)
                break

            ptr1 = ptr1.next
        print("3",ptr2.data)
        ptr2.next = None
        
            

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

print(ll.head.next.next.next.next.next.next.next.data, ll.head.next.next.next.data)
ll.head.next.next.next.next.next.next.next.next = ll.head.next.next.next
ll.detectSnail(ll)
ll.printLinkedList(ll)

print()


#ll.singToCirc()
#ll.printCircularLinkedList(ll)
