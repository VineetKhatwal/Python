counter = 0


class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def insert(root, value):

    newNode = Node(value)

    if root is None:
        root = newNode
        print("ROOT", root.data)
    else:
        insertRecursively(root, newNode)


def insertRecursively(root, newNode):
    global counter

    if (counter == 0):
        if not root.left:
            root.left = newNode
            counter = counter + 1
            return
        else:
            insertRecursively(root.right, newNode)

    if (counter == 0):
        if not root.right:
            root.right = newNode
            counter = counter + 1
            return
        else:
            insertRecursively(root.left, newNode)


def levelOrder(root):

    if root is None:
        return

    queue = []
    queue.append(root)

    while (len(queue) > 0):
        curr = queue.pop(0)

        print(curr.data)

        if curr.left is not None:
            queue.append(curr.left)

        if curr.right is not None:
            queue.append(curr.right)


root = Node(10)

root.left = Node(8)
'''
root.right = Node(2);
root.left.left = Node(3);
root.left.right = Node(5);
root.right.right = Node(4);
'''

print("********** Level Order Recursion **********")
levelOrder(root)
insertRecursively(root, 11)
# insert(root,11)
print("********** Level Order Recursion **********")
levelOrder(root)
