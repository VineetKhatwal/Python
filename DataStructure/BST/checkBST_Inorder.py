class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def levelOrder(root):
    if root is not None:
        levelOrder(root.left)
        print(root.data)
        levelOrder(root.right)


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


prev = -999999
BST = True


def isBST(root):

    global prev
    global BST

    if root is None:
        return True

    isBST(root.left)

    if prev > root.data:
        BST = False

    prev = root.data

    isBST(root.right)

    # print(BST)
    return BST


root = Node(50)
#root.left = Node(520)
insertBST(root, 30)
insertBST(root, 20)
insertBST(root, 40)
insertBST(root, 70)
insertBST(root, 60)
insertBST(root, 80)
insertBST(root, 55)
insertBST(root, 28)
insertBST(root, 19)
root.left.left.left.left = Node(22)


print("********** In Order Travelsal **********")
levelOrder(root)
print("********** IS BST**********")
print(isBST(root))
