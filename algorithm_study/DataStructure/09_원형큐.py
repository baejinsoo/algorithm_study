## 함수 선언부
def isQueueFull():
    global SIZE, queue, front, rear
    if front == (rear+1) % SIZE:
        return True
    return False


def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    return False


def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('큐가 꽉참!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data


def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐가 비었음!')
        return
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


## 전역 변수부
SIZE = 5
queue = [None, None, None, None, None]
front = rear = 0

## 메인 코드부
enQueue('a')
enQueue('b')
enQueue('c')
enQueue('d')
enQueue('e')
print(queue, front)
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(queue)
