class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def areIdentical(root1, root2):

    if (root1 is None and root2 is None):
        return true

    if (root1 is not None and root2 is not None):
        return (root1.data == root2.data and areIdentical(root1.left, root2.left) and areIdentical(root1.right, root2.right))

    return false


root1 = Node(10)
root1.left = Node(8);
root1.right = Node(2); 
root1.left.left = Node(3); 
root1.left.right = Node(5); 
root1.right.right = Node(1);

root2 = Node(10)
root2.left = Node(8);
root2.right = Node(2); 
root2.left.left = Node(3); 
root2.left.right = Node(5); 
root2.right.right = Node(10);

print(areIdentical(root1, root2)
