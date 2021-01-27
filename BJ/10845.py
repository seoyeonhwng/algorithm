import sys
from collections import deque

def push(n):
  queue.append(n)

def pop():
  if queue:
    print(queue.popleft())
  else:
    print('-1')

def size():
  print(len(queue))

def empty():
  if not queue:
    print('1')
  else:
    print('0')

def front():
  if not queue:
    print('-1')
  else:
    print(queue[0])

def back():
  if not queue:
    print('-1')
  else:
    print(queue[-1])

queue = deque()
n = int(input())
for i in range(n):
  cmd = sys.stdin.readline().rstrip().split(' ')
  if cmd[0] == 'push':
    push(cmd[1])
  elif cmd[0] == 'pop':
    pop()
  elif cmd[0] == 'size':
    size()
  elif cmd[0] == 'empty':
    empty()
  elif cmd[0] == 'front':
    front()
  elif cmd[0] == 'back':
    back()

 
