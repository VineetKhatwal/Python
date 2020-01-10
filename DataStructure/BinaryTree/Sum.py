class Node:

    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;

def Sum(root):
    res = root

    if root is None:
        return 0

    return (root.data + Sum(root.left) + Sum(root.right))

        
root = Node(10)
root.left = Node(8);
root.right = Node(-2); 
root.left.left = Node(23); 
root.left.right = Node(5); 
root.right.right = Node(1);

print(Sum(root))
