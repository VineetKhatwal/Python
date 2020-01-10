class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxWidth(root):
    if root is None:
        return False

    q = []
    max_width = 0
    q.append(root)

    while(len(q) > 0):

        width = len(q)
        curr = q.pop(0)
        print("Curr", curr.data)
        if curr.left is not None:
            q.append(curr.left)

        if curr.right is not None:
            q.append(curr.right)

        max_width = max(max_width, width)
        print(max_width)

    return max_width


root1 = Node(10)
root1.left = Node(8)
root1.right = Node(2)
root1.left.left = Node(3)
root1.left.right = Node(5)
root1.right.right = Node(4)
root1.right.left = Node(5)
root1.right.left.left = Node(9)

print(maxWidth(root1))
