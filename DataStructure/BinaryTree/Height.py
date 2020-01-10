class Node:
    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;

def height(root):
    
    if root is None:
        return 0
    
    lheight = height(root.left)
    rheight = height(root.right)

    if (lheight > rheight):
        return lheight + 1
    else:
        return rheight + 1


root = Node(10)
root.left = Node(8); 
root.right = Node(2); 
root.left.left = Node(3); 
root.left.right = Node(5); 
root.right.left = Node(1);
root.left.left.left = Node(9); 

print("********** In Order Recursion **********")
print(height(root));
