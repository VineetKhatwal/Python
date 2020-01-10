fullNode = 0
halfNode = 0
leaf = 0

class Node:

    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;

def leafCount(root):

    global fullNode, halfNode, leaf
    if root:
        
        leafCount(root.left)
        
        if (root.left is not None and root.right is not None):
            fullNode = fullNode + 1
        elif (root.left is not None or root.right is not None):
            halfNode = halfNode + 1       
        elif (root.left is None and root.right is None):
            leaf = leaf + 1
            
        leafCount(root.right)
        
        return fullNode, halfNode, leaf

        
root = Node(10)
root.left = Node(8);
root.right = Node(2); 
root.left.left = Node(3); 
root.left.right = Node(5); 
root.right.right = Node(1);

noOfFullNode =leafCount(root)
print(noOfFullNode)

