# Time: O(n)
# Space O(1)

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
    def insertSLL(self, value, location):
        newNode = Node(value)
        # if no node exists
        if self.head is None:  # O(1)
            self.head = newNode
            self.tail = newNode
        # if a node exists
        else:
            # inserting to the front of the linked list
            if location == 0:  # O(1)
                newNode.next = self.head
                self.head = newNode
            elif location == 1:  # O(1)
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0 
                while index < location - 1:   # O(n)
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                
    # Traverse a SLL
    # Time:  O(n)
    # Space: O(1)
    def traverseSLL(self):
        if self.head is None:                   # O(1)
            print("the SLL does not exist")     # O(1)
        else:
            node = self.head                    # O(1)
            while node is not None:             # O(n)
                print(node.value)
                node = node.next

    # Search for a value in a SLL
    # Time:  O(n)
    # Space: O(1)
    def searchSLL(self, nodeValue):
        # checks if head exists
        if self.head is None:                   # O(1)
            return "The SLL does not exist"     # O(1)
        else:
            # sets variable node to self.head to help with the traversal 
            node = self.head                    # O(1)
            while node is not None:             # O(n)
                # checks for target nodeValue
                if node.value == nodeValue:
                    return node.value           # O(1)
                # moves the variable to the next node in the SLL
                node = node.next                # O(1)
            return "the value does not exist"   # O(1)

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
print([node.value for node in singlyLinkedList])
# singlyLinkedList.traverseSLL()
print(singlyLinkedList.searchSLL(0))
