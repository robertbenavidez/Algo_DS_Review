from collections import deque


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

# preOrderTraveral(newBT)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# inOrderTraversal(newBT)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# def levelOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     custumQueue = [rootNode]
    
    

#     while (not custumQueue):
#         root = custumQueue.pop(0)
#         print(root.data)
#         if (root.data.leftChild is not None):
#             custumQueue.append(root.data.leftChild)
#         if (root.data.rightChild is not None):
#             custumQueue.append(root.data.rightChild)
# levelOrderTraversal(newBT)


# postOrderTraversal(newBT)
# Code taken from GeeksforGeeks
# In the tutorial they say it is a two Queue implementation
# but rather it is a two Stack implementation
def levelOrder(node):
        q1 = [] # Queue 1
        q2 = [] # Queue 2
        q1.append(node)
         
        """Executing loop until both the
        queues become empty"""
        while(len(q1) > 0 or len(q2) > 0):
         
            """Empty string to concatenate
            the string for q1"""
            concat_str_q1 = ''
            while(len(q1) > 0):
                 
                """Popped node at the first
                pos in queue 1 i.e q1"""
                popped_node = q1.pop(0)
                concat_str_q1 += popped_node.data +' '
                 
                """Pushing left child of current
                node in first queue into second queue"""
                if popped_node.leftChild:
                    q2.append(popped_node.leftChild)
                     
                """Pushing right child of current node
                in first queue into second queue"""
                if popped_node.rightChild:
                    q2.append(popped_node.rightChild)
            print( str(concat_str_q1))
            concat_str_q1 = ''
             
            """Empty string to concatenate the
            string for q1"""
            concat_str_q2 = ''
            while (len(q2) > 0):
             
                """Poped node at the first pos
                in queue 1 i.e q1"""
                popped_node = q2.pop(0)
                concat_str_q2 += popped_node.data + ' '
                 
                """Pushing left child of current node
                in first queue into first queue"""
                if popped_node.leftChild:
                    q1.append(popped_node.leftChild)
                 
                """Pushing right child of current node
                in first queue into first queue"""
                if popped_node.rightChild:
                    q1.append(popped_node.rightChild)
            print(str(concat_str_q2))
            concat_str_q2 = ''

# levelOrder(newBT)