class Node:
    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;

def search(root, target):
    
    if root is None:
        return False

    if root.data == target:
        return True
    else:
        return (search(root.left, target) or search(root.right, target))


root = Node(10)
root.left = Node(8)
root.right = Node(2) 
root.left.left = Node(3)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.right.left = Node(1)
root.right.left.right = Node(9)
print(search(root,10));
print(search(root,9));
print(search(root,3));
print(search(root,4));
print(search(root,8));
