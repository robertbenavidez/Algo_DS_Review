class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node.next == self.tail.next:
                break

    # creates CSLL
    # Time: O(1) Space: O(1)
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"

# Insertion of a node in CSLL

    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "the node has been succesfully inserted"


circularSLL = CircularSLL()
print(circularSLL.createCSLL(1))
circularSLL.insertCSLL(0, 0)
circularSLL.insertCSLL(2, 1)
circularSLL.insertCSLL(2, 2)
circularSLL.insertCSLL(3, 2)
circularSLL.insertCSLL(1, 0)

print([node.value for node in circularSLL])
