class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")


def levelOrderRec(root):
    if root:
        queue = []
        queue.append(root)

        while (len(queue) > 0):
            curr = queue.pop(0)
            print(curr.data, end=" ")

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
    else:
        return


def preOrderRec(root):
    if root:
        stack = []
        stack.append(root)

        while (len(stack) > 0):
            curr = stack.pop()
            print(curr.data, end=" ")

            if curr.right:
                stack.append(curr.right)

            if curr.left:
                stack.append(curr.left)
    else:
        return


def inOrderRec(root):
    if root:
        stack = []
        curr = root
        while (curr or len(stack) > 0):
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            print(curr.data, end=" ")
            curr = curr.right
    else:
        return


def maxElement(root):
    maxValue = -999999999999

    if root is None:
        return maxValue

    leftMax = maxElement(root.left)
    rightMax = maxElement(root.right)

    maxValue = max(leftMax, rightMax)
    maxValue = max(maxValue, root.data)

    return maxValue


def minElement(root):
    minValue = 999999999999

    if root is None:
        return minValue

    leftMin = minElement(root.left)
    rightMin = minElement(root.right)

    minValue = min(leftMin, rightMin)
    minValue = min(minValue, root.data)

    return minValue


def searchElement(root, target):
    if root is None:
        return False

    if root.data == target:
        return True
    else:
        return (searchElement(root.left, target) or searchElement(root.right, target))


def size(root):
    if root is None:
        return 0

    return (1 + size(root.left) + size(root.right))


def Sum(root):
    if root is None:
        return 0

    return (root.data + Sum(root.left) + Sum(root.right))


def Height(root):
    if root is None:
        return 0

    lHeight = Height(root.left)
    rHeight = Height(root.right)

    return max(lHeight, rHeight) + 1


def deleteTree(root):
    root = None


root = Node(10)
root.left = Node(8)
root.right = Node(-2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(20)
root.left.left.left = Node(13)

print("********** Pre Order  **********")
preOrder(root)
print()
print("********** In Order   **********")
inOrder(root)
print()
print("********** Post Order **********")
postOrder(root)
print()

print("********** Level Order Recursive **********")
levelOrderRec(root)
print()

print("********** Pre Order Recursive **********")
preOrderRec(root)
print()


print("********** In Order Recursive **********")
inOrderRec(root)
print()

print("********** Max Element **********")
print(maxElement(root))
print()

print("********** Min Element **********")
print(minElement(root))
print()


print("********** Search Element **********")
print(searchElement(root, -2))
print(searchElement(root, -29))
print()

print("********** Size **********")
print(size(root))
print()

print("********** Sum **********")
print(Sum(root))
print()

print("********** Height **********")
print(Height(root))
print()


print("********** Deletion **********")
deleteTree(root)
print()

print("********** Pre Order  **********")
preOrder(root)
print()
