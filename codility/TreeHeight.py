# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task
import collections

def solution(T):
    # write your code in Python 3.6
    if not T:
        return -1
        
    height = 0
    queue = collections.deque([T])
    
    while queue:
        height += 1
        for _ in range(len(queue)):
            v = queue.popleft()
            if v.l:
                queue.append(v.l)
            if v.r:
                queue.append(v.r)
                
    return height - 1
