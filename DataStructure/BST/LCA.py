class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def preOrder(root):
    if root:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


def insertBST(root, data):

    newNode = Node(data)

    if root is None:
        root = newNode
        return root

    if data < root.data:
        root.left = insertBST(root.left, data)
    elif data > root.data:
        root.right = insertBST(root.right, data)

    return root


def lcaIter(root, n1, n2):

    while root:

        # If both n1 and n2 are smaller than root, then LCA lies in left
        if n1 < root.data and n2 < root.data:
            root = root.left

        # If both n1 and n2 are greater than root, then LCA lies in right
        elif n1 > root.data and n2 > root.data:
            root = root.right

        else:
            break

    return root


def lcaRec(root, p, q):

    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA lies in left
    if(p < root.data and q < root.data):
        return lcaRec(root.left, p, q)

    # If both n1 and n2 are greater than root, then LCA lies in right
    if(p > root.data and q > root.data):
        return lcaRec(root.right, p, q)

    return root


root = Node(50)
insertBST(root, 30)
insertBST(root, 20)
insertBST(root, 40)
insertBST(root, 70)
insertBST(root, 45)
insertBST(root, 60)
insertBST(root, 80)
insertBST(root, 55)
insertBST(root, 28)
insertBST(root, 19)
insertBST(root, 78)
insertBST(root, 90)


print("********** In Order Recursion **********")
inOrder(root)
print()

print("********** LCA Iter **********")
print(lcaIter(root, 19, 90).data)
print(lcaIter(root, 19, 28).data)
print(lcaIter(root, 19, 40).data)
print(lcaIter(root, 30, 40).data)
print(lcaIter(root, 50, 40).data)
print(lcaIter(root, 80, 45).data)
print(lcaIter(root, 70, 90).data)
print(lcaIter(root, 90, 70).data)
print(lcaIter(root, 45, 55).data)

print("********** LCA Rec **********")
print(lcaRec(root, 19, 90).data)
print(lcaRec(root, 19, 28).data)
print(lcaRec(root, 19, 40).data)
print(lcaRec(root, 30, 40).data)
print(lcaRec(root, 50, 40).data)
print(lcaRec(root, 80, 45).data)
print(lcaRec(root, 70, 90).data)
print(lcaRec(root, 90, 70).data)
print(lcaRec(root, 45, 55).data)
