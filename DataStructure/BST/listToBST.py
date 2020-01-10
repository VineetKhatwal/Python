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

def listToBST(list, l, r):
    if l>r:
        return

    m = int((l+r)/2)
    newNode = Node(list[m])
    newNode.left = listToBST(list, l, m-1);
    newNode.right = listToBST(list, m+1, r);

    return newNode;

    
list = [1,2,5,6,3,7,8,12]
list.sort()
length = len(list) - 1
root = listToBST(list,0,length)
inOrder(root)

