counter = 0


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def insertNode(root, data):
    newNode = Node(data)

    if root is None:
        root = newNode
        return

    queue = []
    queue.append(root)

    while (len(queue) > 0):

        curr = queue.pop(0)

        if curr.left:
            queue.append(curr.left)
        else:
            curr.left = newNode
            break

        if curr.right:
            queue.append(curr.right)
        else:
            curr.right = newNode
            break


def Height(root):
    if root is None:
        return 0

    return max(Height(root.left), Height(root.right)) + 1


def minDepth(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    if root.left is None:
        return minDepth(root.right) + 1

    if root.right is None:
        return minDepth(root.left) + 1

    return min(minDepth(root.right), minDepth(root.left)) + 1


def Diameter(root):
    if root is None:
        return 0

    lHeight = Height(root.left)
    rHeight = Height(root.right)

    return (lHeight + rHeight + 1)

# Leet Code :  257


def printPath(root):
    s = []
    printPathRecursively(root, s)


def printPathRecursively(root, s):
    if root is None:
        return

    s.append(root.data)

    if root.left is None and root.right is None:
        printList(s)

    printPathRecursively(root.left, s)
    printPathRecursively(root.right, s)
    s.pop()


def printList(s):
    for i in s:
        print(i, end=" ")
    print()


def hasPathSum(root, sum):

    if root is None:
        return False

    sum = sum - root.data

    if (sum == 0 and root.left is None and root.right is None):
        return True
    else:
        return (hasPathSum(root.left, sum) or hasPathSum(root.right, sum))

    return False

# 100, 101


def maxWidth(root):

    if root is None:
        return 0

    maxW = 0
    width = 0
    q = []
    q.append(root)

    while(len(q) > 0):
        width = len(q)
        curr = q.pop(0)

        if curr.left:
            q.append(curr.left)

        if curr.right:
            q.append(curr.right)

        maxW = max(maxW, width)

    return maxW


def maxLevelSum(root):

    if root is None:
        return 0

    maxSum = root.data
    q = []
    q.append(root)

    while q:
        curr_sum = 0
        l = len(q)
        while l > 0:
            curr = q.pop(0)
            curr_sum = curr_sum + curr.data

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

            l = - 1

        maxSum = max(maxSum, curr_sum)

    return maxSum


root = Node(10)
root.left = Node(8)
root.right = Node(-2)
#root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(1)

print("********** Level Order  **********")
levelOrderRec(root)
print()

print("********** Insert  **********")
insertNode(root, 24)
levelOrderRec(root)
print()

insertNode(root, -9)
print()
levelOrderRec(root)
print()

insertNode(root, 19)
print()
levelOrderRec(root)
print()

root.left.left.left.left = Node(10)

print("********** Level Order  **********")
levelOrderRec(root)
print()

print("********** Height **********")
print(Height(root))
print()


print("********** Minumum Height **********")
print(minDepth(root))
print()


print("********** Diameter  **********")
print(Diameter(root))
print()

print("********** Paths  **********")
printPath(root)
print()

print("********** Paths  **********")
print(hasPathSum(root, 181))
print()

print("********** Level Order  **********")
levelOrderRec(root)
print()

print("********** Max Width  **********")
print(maxWidth(root))
print()

print("********** Max Level Sum  **********")
print(maxLevelSum(root))
print()
