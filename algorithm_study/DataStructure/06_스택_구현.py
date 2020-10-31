# 스택의 초기화
stack = [None, None, None, None, None]
top = -1

# Push
top += 1
stack[top] = 'A'

top += 1
stack[top] = 'B'

top += 1
stack[top] = 'C'

print(stack)

# POP
data = stack[top]
stack[top] = None
top -= 1
print(stack)

data = stack[top]
stack[top] = None
top -= 1
print(stack)

data = stack[top]
stack[top] = None
top -= 1
print(stack)
