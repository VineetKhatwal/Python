class Node:
    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;

def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data, end =" ")
        inOrder(root.right)

def insertBST(root, data):

    newNode = Node(data)
    
    if root is None:
        root = newNode
        return root
    
    if data < root.data:
        root.left = insertBST(root.left, data)
    elif data > root.data:
        root.right = insertBST(root.right, data)
        
    return root

def printMax(root):
    maxValue = 0
    if root is None:
        return

    while(root):
        maxValue = root.data
        root = root.right

    return maxValue

def printMin(root):
    minValue = 0
    if root is None:
        return

    while(root):
        minValue = root.data
        root = root.left

    return minValue

root = Node(50)
insertBST(root,30)
insertBST(root,20)
insertBST(root,40); 
insertBST(root,70); 
insertBST(root,60); 
insertBST(root,80);
insertBST(root,55); 
insertBST(root,28); 
insertBST(root,19);

print("********** Level Order Recursion **********")
inOrder(root)
print()
print("********** MAX **********")
print(printMax(root))
print("********** MIN **********")
print(printMin(root))
