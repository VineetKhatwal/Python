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

    def Palindrome(self):
        pl_list = []
        while self.head:
            pl_list.append(self.head)
            self.head = self.head.next

        length = len(pl_list)

        for i in range(length // 2):
            if pl_list[i].data != pl_list[length - 1 - i].data:
                return False

        return True


ll = LinkedList()
ll.insertAtBegin(0)
ll.insertAtBegin(5)
ll.insertAtBegin(10)
ll.insertAtBegin(15)
ll.insertAtBegin(10)
ll.insertAtBegin(5)
ll.insertAtBegin(0)
ll.insertAtBegin(10)
#ll.printLinkedList(ll)
print()
print(ll.Palindrome())

print()
