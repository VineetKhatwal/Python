class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printAllPath(root):
    s = []
    printPathRecursively(root, s)

def printPathRecursively(root, s):

    if root is None:
       return

    s.append(root.data)

    if (root.left is None and root.right is None):
        printPath(s)

    printPathRecursively(root.left, s)
    printPathRecursively(root.right, s)
    s.pop()

def printPath(s):

    for i in s:
        print(i, end =" ")
    print()
    

root1 = Node(10)
root1.left = Node(8)
root1.right = Node(2) 
root1.left.left = Node(3)
root1.left.right = Node(5) 
root1.right.right = Node(4)
root1.right.left = Node(5)
root1.right.left.left = Node(9)

print(printAllPath(root1))
