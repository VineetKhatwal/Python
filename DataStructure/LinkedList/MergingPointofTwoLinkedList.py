class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def getCount(self, head):
        if not head:
            return 0

        count = 0
        while(head):
            head = head.next
            count += 1
        return count

    def getIntersectionPoint(self, d, head1, head2):
        print("Finding Intersection Points")
        print(head1.data, head2.data)

        i = 0

        while(i < d):
            head1 = head1.next
            i += 1

        while (head1 and head2):
            if head1.data == head2.data:
                return (head1.data, head2.data)
            head1 = head1.next
            head2 = head2.next

    def getIntersectionNode(self, ll, head1, head2):
        print("In Intersection Method")
        d1 = ll.getCount(head1)
        d2 = ll.getCount(head2)

        if d1 > d2:
            return ll.getIntersectionPoint(d1 - d2, head1, head2)
        else:
            return ll.getIntersectionPoint(d2 - d1, head2, head1)

    def getMergingPoint(self, headA, headB):

        if headA is None or headB is None:
            return None

        ptr_one = headA
        ptr_two = headB

        while ptr_one != ptr_two:
            if ptr_one:
                ptr_one = ptr_one.next
            else:
                ptr_one = headB

            if ptr_two:
                ptr_two = ptr_two.next
            else:
                ptr_two = headA
        return ptr_one


list = LinkedList()

list.head1 = Node(4)
list.head1.next = Node(1)
list.head1.next.next = Node(8)
list.head1.next.next.next = Node(4)
list.head1.next.next.next.next = Node(5)


list.head2 = Node(5)
list.head2.next = Node(0)
list.head2.next.next = Node(1)
list.head2.next.next.next = Node(8)
list.head2.next.next.next.next = Node(4)
list.head2.next.next.next.next.next = Node(5)

#print("Intersection Point = ", list.getIntersectionNode(list, list.head1, list.head2))

print("Intersection Point = ", list.getMergingPoint(list.head1, list.head2))
