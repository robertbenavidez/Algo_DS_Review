class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    
    def insert(self, value):
        if value < self.value:
            # the new value, must go left
            if self.left is None:
                # create a new node as a left child of current node
                self.left = BinaryTreeNode(value)
            else:
                self.left.insert(value)

        else:
            # the value must go right
            if self.right is None:
                self.right = BinaryTreeNode(value)
            else:
                self.right.insert(value)

    
    

def isBalancedHelper(root):
    if root is None:
        return 0
    
    leftHeight = isBalancedHelper(root.left)
    rightHeight = isBalancedHelper(root.right)

    if leftHeight == -1:
        return -1
    if rightHeight == -1:
        return -1
    if abs(leftHeight-rightHeight)>1:
        return -1
    
    return max(leftHeight, rightHeight) + 1

def balancedBinaryTree(root):
    return isBalancedHelper(root) > -1

root = BinaryTreeNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(13)

def printTree(node, level=0):
        if node != None:
            printTree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            printTree(node.left, level + 1)

printTree(root)
print(balancedBinaryTree(root))


