counter = 0

class Node:
    
    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;

def insert(root, value):

    newNode = Node(value)
    
    if root is None:
        return
    
    queue = []
    queue.append(root)

    while (len(queue) > 0):
        curr = queue.pop(0)

        if curr.left is not None:
            queue.append(curr.left)
        else:
            curr.left = newNode
            break
            
        if curr.right is not None:
            queue.append(curr.right)
        else:
            curr.right = newNode
            break
            
    

def levelOrder(root):

    if root is None:
        return
    
    queue = []
    queue.append(root)

    while (len(queue) > 0):
        curr = queue.pop(0)

        print(curr.data)

        if curr.left is not None:
            queue.append(curr.left)
            
        if curr.right is not None:
            queue.append(curr.right)

        
root = Node(10)
root.left = Node(8);
root.right = Node(2); 
root.left.left = Node(3); 
root.left.right = Node(5); 
root.right.right = Node(4);


print("********** Level Order Recursion **********")
levelOrder(root)
insert(root,11)
insert(root,13)
print("********** Level Order Recursion **********")
levelOrder(root)
