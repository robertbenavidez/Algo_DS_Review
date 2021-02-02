class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # Insert into Linked List
    # def insertSLL(self, value, location):
    #     newNode = Node(value)
    #     # if no node exists
    #     if self.head is None:
    #         self.head = newNode
    #         self.tail = newNode
    #     # if a node exists
    #     else:
    #         # inserting to the front of the linked list
    #         if location == 0:
    #             newNode.next = self.head
    #             self.head = newNode
    #         elif location == 1:
    #             newNode.next = Node
    #             self.head =
            


singlyLinkedList = SLinkedList()
print([node.value for node in singlyLinkedList])
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2
