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


# Leet Code 236


def lca(root, p, q):

    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root

    if left is None:
        return right

    if right is None:
        return left


root = Node(10)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(11)
root.right.right = Node(17)
root.right.right.left = Node(27)
root.right.right.right = Node(18)

lowestCommonAncestor = lca(root, root.right.left, root.right.right)
print(lowestCommonAncestor.data)
print()


lowestCommonAncestor = lca(root, root.left.left, root.left.right)
print(lowestCommonAncestor.data)
print()


lowestCommonAncestor = lca(root, root.left.left, root.right.right.left)
print(lowestCommonAncestor.data)
print()


lowestCommonAncestor = lca(root, root.right, root.right.right.right)
print(lowestCommonAncestor.data)
print()


lowestCommonAncestor = lca(root, root, root.left.right)
print(lowestCommonAncestor.data)
print()
