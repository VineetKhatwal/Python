class Node:
    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;

def inOrder(root):
    
    if root is None:
        return

    stack = []
    curr = root;

    while(curr is not None or len(stack) > 0):
        while(curr is not None):
            stack.append(curr)
            curr = curr.left;

        curr = stack.pop();
        print(curr.data)
        curr = curr.right;


root = Node(10)
root.left = Node(8); 
root.right = Node(2); 
root.left.left = Node(3); 
root.left.right = Node(5); 
root.right.left = Node(1);

print("********** In Order Recursion **********")
inOrder(root)
