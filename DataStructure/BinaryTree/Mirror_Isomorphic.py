class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def checkMirror(root1, root2):

    # Leet Code 101

    if (root1 is None and root2 is None):
        return True

    if (root1 is None or root2 is None):
        return False

    if (root1.data != root2.data):
        print(root1.data, root2.data)
        return False

    if (checkMirror(root1.left, root2.right) and checkMirror(root1.right, root2.left)):
        return True

    return False


root1 = Node(10)
root1.left = Node(8)
root1.right = Node(2)
root1.left.left = Node(3)
root1.left.right = Node(5)
root1.right.right = Node(1)

root2 = Node(10)
root2.left = Node(2)
root2.right = Node(8)
root2.left.left = Node(1)
root2.right.left = Node(5)
root2.right.right = Node(3)

print(checkMirror(root1, root2))
