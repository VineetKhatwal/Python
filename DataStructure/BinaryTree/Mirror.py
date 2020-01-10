counter = 0


class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


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


def mirror(root):

    if root is None:
        return root

    mirror(root.left)
    mirror(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(1)


print("********** Tree: Level Order Recursion **********")
levelOrder(root)

mirror(root)

print("********** Mirror Tree : Level Order Recursion **********")
levelOrder(root)
