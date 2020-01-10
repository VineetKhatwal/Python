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


def deleteNode(root, data):

    if root is None:
        return

    if data < root.data:
        root.left = deleteNode(root.left, data)
    elif data > root.data:
        root.right = deleteNode(root.right, data)
    else:

        # Node with only one child or no child
        if (root.left is None):
            return root.right
        if(root.right is None):
            return root.left

        # Node with two child
        root.data = findMax(root.right)
        root.right = deleteNode(root.right, root.data)

    return root


def findMax(root):
    maxValue = 0
    if root is None:
        return

    while(root):
        maxValue = root.data
        root = root.right

    return maxValue


root = Node(50)
insertBST(root, 30)
insertBST(root, 20)
insertBST(root, 40)
insertBST(root, 70)
insertBST(root, 60)
insertBST(root, 80)
insertBST(root, 55)
insertBST(root, 28)
insertBST(root, 19)


print("********** In Order Travelsal **********")
levelOrder(root)
print("********** IS BST**********")
deleteNode(root, 70)
print("********** In Order Travelsal after deletion **********")
levelOrder(root)
