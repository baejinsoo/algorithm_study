# 큐의 이해
queue = [None, None, None]
front = rear = -1

rear += 1
queue[rear] = 'A'

rear += 1
queue[rear] = 'B'

rear += 1
queue[rear] = 'C'

print(queue)

front += 1
data = queue[front]
queue[front] = None
print(data)

front += 1
data = queue[front]
queue[front] = None
print(data)

front += 1
data = queue[front]
queue[front] = None
print(data)
print(queue)
