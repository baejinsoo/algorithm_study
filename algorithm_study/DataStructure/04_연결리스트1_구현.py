class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNode(head):
    current = head
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '사나'
node2.link = node3

node4 = Node()
node4.data = '쯔위'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

printNode(node1)

newNode = Node()
newNode.data = '진수'
newNode.link = node2.link
node2.link = newNode

printNode(node1)

node2.link = newNode.link
del(newNode)
printNode(node1)
