class Node:
    def __init__(self, data):
        self.data = data;
        self.right = None
        self.left = None

def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)

root = Node(10)
root.left = Node(8); 
root.right = Node(2); 
root.left.left = Node(3); 
root.left.right = Node(5); 
root.right.left = Node(1);

print("********** Pre Order Recursion **********")
preOrder(root)
print()
print("**********  In Order Recursion **********")
inOrder(root)
print()
print("********** Post Order Recursion *********")
postOrder(root)


