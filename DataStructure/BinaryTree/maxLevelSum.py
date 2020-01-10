class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def maxLevelSum(root):

    if root is None:
        return 0

    maxSum = root.data

    q = []
    q.append(root)

    while q:
        # OR while len(q) > 0:
        curr_sum = 0
        l = len(q)
        while l > 0:
            curr = q.pop(0)

            curr_sum = curr_sum + curr.data

            if (curr.left):
                q.append(curr.left)

            if (curr.right):
                q.append(curr.right)

            l -= 1

        maxSum = max(maxSum, curr_sum)

    return maxSum


root = Node(10)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(10)
root.right.right = Node(17)
root.right.right.left = Node(26)
root.right.right.right = Node(18)

print("Max Root Level Sum =", maxLevelSum(root))
