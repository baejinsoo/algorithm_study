## 함수 선언부
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


def insert_node(findData, insertData):
    global memory, head, pre, current

    if findData == head.data: # 첫 노드가 찾는 값 일때
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    # 두번쩨 노드 이후 일때...
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    # 마지막까지 못찾았을 때..(마지막에 삽입)
    node = Node()
    node.data = insertData
    current.link = node


def delete_node(findData):
    global memory, head, pre, current
    if findData == head.data: # 첫노드가 찾는 값일때
        current = head
        head = head.link
        del(current)
        return
    # 두번째 노드 이후를 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            pre.link = current.link
            del(current)
            return


def find_node(findData):
    # 찾으면 True, 못찾으면 False 리턴
    global memory, head, pre, current
    if findData == head.data:
        return True
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            return True
    return False

## 전역 변수부
memory = []
head, pre, current = None, None, None
dataArr = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드부
if __name__ == '__main__':
    # 첫번째 노드
    node = Node()
    node.data = dataArr[0]
    head = node # 헤드 지점(*중요)
    memory.append(node)

    # 두 번째 노드부터 ...
    for data in dataArr[1:]:
        pre = node # 이전 노드 기억(*중요)
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNode(head)
    insert_node('다현', '화사')
    printNode(head)
    insert_node('사나', '솔라')
    printNode(head)
    insert_node('마동석', '문별')
    printNode(head)
    delete_node('화사')
    printNode(head)
    delete_node('솔라')
    printNode(head)
    print(find_node('정연'))
    print(find_node('다현'))
