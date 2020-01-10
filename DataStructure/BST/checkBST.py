class Node:
    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;

def levelOrder(root):
    if root is not None:
        levelOrder(root.left)
        print(root.data)
        levelOrder(root.right)

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

def isBST(root):
    
    if root is None:
        return True

    if (root.left and (maxValueInTree(root.left) > root.data)):
        return False

    if (root.right and (minValueinTree(root.right) < root.data)):
        return False

    if (not(isBST(root.left)) or not(isBST(root.right))):
        return False

    return True

def maxValueInTree(root):
    maxValue = 0
    if root is None:
        return

    while(root):
        maxValue = root.data
        root = root.right

    return maxValue

def minValueinTree(root):
    minValue = 0
    if root is None:
        return

    while(root):
        minValue = root.data
        root = root.left

    return minValue
    

root = Node(50)
#root.left = Node(52)
insertBST(root,30)
insertBST(root,20)
insertBST(root,40); 
insertBST(root,70); 
insertBST(root,60); 
insertBST(root,80);
insertBST(root,55); 
insertBST(root,28); 
insertBST(root,19);


print("********** In Order Travelsal **********")
levelOrder(root)
print("********** IS BST**********")
print(isBST(root))
