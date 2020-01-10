class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def ancestor(root, data):

    if (root is None):
        return False

    if (root.data == data):
        return True

    left = ancestor(root.left, data)
    right = ancestor(root.right, data)

    if (left or right):
        print(root.data, end=" ")
        return True

    return False


root = Node(10)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(10)
root.right.right = Node(17)
root.right.right.left = Node(27)
root.right.right.right = Node(18)

ancestor(root, 27)
print()
