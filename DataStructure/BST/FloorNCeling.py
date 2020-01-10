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


def Floor(root, data):

    if root is None:
        return 999999999999

    if root.data == data:
        return data

    if data < root.data:
        return Floor(root.left, data)

    floorVal = Floor(root.right, data)

    if floorVal <= data:
        return floorVal
    else:
        return root.data


def Ceiling(root, data):

    if root is None:
        return -999999999999

    if root.data == data:
        return data

    if data > root.data:
        return Ceiling(root.right, data)

    ceilingVal = Ceiling(root.left, data)

    if ceilingVal >= data:
        return ceilingVal
    else:
        return root.data


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

print("********** FLOOR Values **********")

print(Floor(root, 17))
print(Floor(root, 46))
print(Floor(root, 38))
print(Floor(root, 40))
print(Floor(root, 22))
print(Floor(root, 82))
print(Floor(root, 88))
print(Floor(root, 94))

print("********** CEILING Values **********")

print(Ceiling(root, 17))
print(Ceiling(root, 46))
print(Ceiling(root, 38))
print(Ceiling(root, 40))
print(Ceiling(root, 22))
print(Ceiling(root, 82))
print(Ceiling(root, 88))
print(Ceiling(root, 94))
