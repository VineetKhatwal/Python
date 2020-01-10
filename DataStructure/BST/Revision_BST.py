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


def searchBST(root, data):

    if root is None:
        return False

    if root.data == data:
        return True

    if data < root.data:
        return searchBST(root.left, data)
    elif data > root.data:
        return searchBST(root.right, data)


prev = -999999999999
isBSTTree = True


def isBSTInorder(root):

    global prev
    global isBSTTree

    if root is None:
        return True

    isBSTInorder(root.left)
    if prev > root.data:
        isBSTTree = False
    prev = root.data
    isBSTInorder(root.right)

    return isBSTTree


def maxValBST(root):

    while root.right:
        root = root.right

    return root.data


def minValBST(root):

    while root.left:
        root = root.left

    return root.data


def isBSTRec(root):                                             # O(n ^ 2)

    if root is None:
        return True

    if root.left and maxValBST(root.left) > root.data:
        return False

    if root.right and maxValBST(root.right) < root.data:
        return False

    if not(isBSTRec(root.left)) or not(isBSTRec(root.right)):
        return False

    return True


def isBST(root, min, max):                                      # O(n)

    if root is None:
        return True

    return (root.data > min and root.data < max and isBST(root.left, min, root.data) and isBST(root.right, root.data, max))

# Leet COde - 450


def deleteNode(root, data):

    if root is None:
        return None

    if data < root.data:
        root.left = deleteNode(root.left, data)
    elif data > root.data:
        root.right = deleteNode(root.right, data)
    else:
        if root.left and root.right:
            root.data = minValBST(root.right)
            root.right = deleteNode(root.right, root.data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

    return root


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
# To check the negative condition in the BST is valid
#root.left.left.left.left = Node(22)

print("********** Pre Order Recursion **********")
preOrder(root)
print()
print()

print("********** In Order Recursion **********")
inOrder(root)
print()
print()

print("********** Recursive Search : Found **********")
print(searchBST(root, 50))
print(searchBST(root, 30))
print(searchBST(root, 20))
print(searchBST(root, 40))
print(searchBST(root, 70))
print(searchBST(root, 60))
print(searchBST(root, 80))
print(searchBST(root, 55))
print(searchBST(root, 28))
print(searchBST(root, 19))
print("********** Recursive Search : Not Found **********")
print(searchBST(root, 51))
print(searchBST(root, 49))
print(searchBST(root, -10))
print(searchBST(root, 99))
print(searchBST(root, 10))

print("********** In Order Recursion **********")
inOrder(root)
print()
print()
print("********** Is BST : Inorder **********")
print(isBSTInorder(root))

prev = -999999999999

print("********** Is BST : Recursive (O(n)^2) **********")
print(isBSTRec(root))

print("********** Is BST : (O(n)) **********")
print(isBST(root, -999999999999, 999999999999))

print("********** MaxValue **********")
print(maxValBST(root))

print("********** MinValue **********")
print(minValBST(root))

print("********** In Order Recursion **********")
inOrder(root)
print()

print("********** Delete Node : 34 **********")
deleteNode(root, 34)
inOrder(root)
print()

#deleteNode(root, 55)
#deleteNode(root, 80)
#deleteNode(root, 50)
#deleteNode(root, 20)
insertBST(root, 75)
inOrder(root)
print()
deleteNode(root, 70)
inOrder(root)
print()
