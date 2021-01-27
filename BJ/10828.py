import sys

def push(input_x):
    stack.append(input_x)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    top = len(stack) - 1
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[top])


stack = []
num = int(input())

for i in range(num):
    cmd = sys.stdin.readline().rstrip().split(" ")
    if cmd[0] == 'push':
        input_x = int(cmd[1])
        push(input_x)
    elif cmd[0] == 'pop':
        pop()
    elif cmd[0] == 'size':
        size()
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'top':
        top()
