class Node:
    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;

def diameter(root):
    
    if root is None:
        return 0

    l_tree_ht = height(root.left)
    r_tree_ht = height(root.right)
    return ( l_tree_ht + r_tree_ht +1)

def height(root):
    
    if root is None:
        return 0
    
    return (1 + max(height(root.left) ,height(root.right)))


root = Node(10)
root.left = Node(8)
root.right = Node(2) 
root.left.left = Node(3)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.right.left = Node(1)
root.right.left.right = Node(9)

print("********** Diamater **********")
print(diameter(root));
