class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def hasPathSum(root, sum):

    # Leet Code 112 and 113

    if root is None:
       return False

    sum = sum - root.data

    if (sum ==0 and root.left is None and root.right is None):
        return True
    else:
        return (hasPathSum(root.left, sum) or hasPathSum(root.right, sum))


root1 = Node(10)
root1.left = Node(8)
root1.right = Node(2)
root1.left.left = Node(3)
root1.left.right = Node(5)
root1.right.right = Node(4)
root1.right.left = Node(5)

print(hasPathSum(root1, 17))
