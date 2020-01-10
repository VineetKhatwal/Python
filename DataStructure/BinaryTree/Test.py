class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def testFunction(root):
    if root is None:
        return

    width = 0;
    
    q = []
    q.append(root)

    while q:
        size = len(q)
        curr = q.pop(0)
        #print(curr.data)
        
        if curr.left:
            q.append(curr.left)

        if curr.right:
            q.append(curr.right)

        width = max(width, size)

    return width

def hasSum(root, sum):
    if root is None:
        return False
    
    sum = sum - root.data

    if (sum ==0 and root.left is None and root.right is None):
        return True
    else:
        return (hasSum(root.left, sum) or hasSum(root.right, sum))

def allPath(root):

    arr = []
    printRecursively(root, arr)

def printRecursively(root, arr):
    if root is None:
        return

    arr.append(root.data)
    if (root.left is None and root.right is None):
            for i in range(len(arr)):
                print(arr[i], end=" ")
            print()

    printRecursively(root.left, arr)
    printRecursively(root.right, arr)
    arr.pop()

def maxLevelSum(root):

    if root is None:
        return

    maxSum = root.data
    
    q=[]
    q.append(root)

    while q:
        currSum = 0
        l = len(q)
        while(l>0):
            curr = q.pop(0)
            
            currSum = currSum + curr.data

            if (curr.left):
                q.append(curr.left)

            if (curr.right):
                q.append(curr.right)

            l -= 1

        maxSum = max(maxSum, currSum)
        
    return maxSum
            
        

root = Node(10)
root.left = Node(8); 
root.right = Node(22); 
root.left.left = Node(3); 
root.left.right = Node(5); 
root.right.left = Node(10);
root.right.right = Node(17);
root.right.right.left = Node(27);
root.right.right.right = Node(18);
#print(testFunction(root))
#print(hasSum(root,42))
#allPath(root)
print(maxLevelSum(root))
