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

        


root = Node(10)
root.left = Node(8); 
root.right = Node(2); 
root.left.left = Node(3); 
root.left.right = Node(5); 
root.right.left = Node(1);

print("********** Level Order Recursion **********")
levelOrder(root)
