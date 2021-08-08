class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks ")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
# print(newBT.leftChild.data)
# print(newBT.rightChild.data)

def preOrderTraveral(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraveral(rootNode.leftChild)
    preOrderTraveral(rootNode.rightChild)

preOrderTraveral(newBT)