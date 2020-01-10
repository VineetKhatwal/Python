class Node:
    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;

def levelOrder(root):
    
    if root is None:
        return

    stack = []
    stack.append(root)

    while (len(stack) > 0):
        curr = stack.pop(0)

        print(curr.data)

        if curr.left is not None:
            stack.append(curr.left)
            
        if curr.right is not None:
            stack.append(curr.right)

def removeHalfNodes(root):

    if root is None:
        return None

    root.left = removeHalfNodes(root.left)
    root.right = removeHalfNodes(root.right)

    if root.left is None and root.right is None:
        return root

    if root.left is None:
        return root.right

    if root.right is None:
        return root.left

    return root
    


root = Node(10)
root.left = Node(8); 
root.right = Node(2); 
root.left.left = Node(3); 
root.left.right = Node(5); 
root.right.left = Node(1);

print("********** Level Order Recursion **********")
levelOrder(root)
removeHalfNodes(root)
print("********** Level Order Recursion **********")
levelOrder(root)
