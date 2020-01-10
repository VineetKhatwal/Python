class Node:

    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;

def Max(root):
    
    maxValue = -999999999999

    if root is None:
        return maxValue

    lMax = Max(root.left)
    rMax = Max(root.right)

    maxValue = max(lMax, rMax)
    maxValue = max(maxValue, root.data)

    return maxValue

def Min(root):
    res = root

    if root is None:
        return 999999999999

    lMax = Min(root.left)
    rMax = Min(root.right)

    if lMax < rMax:
        minValue = lMax
    else:
        minValue = rMax

    if res.data < minValue:
        minValue = res.data

    return minValue

        
root = Node(10)
root.left = Node(8);
root.right = Node(-2); 
root.left.left = Node(23); 
root.left.right = Node(5); 
root.right.right = Node(1);

print(Max(root))
print(Min(root))
