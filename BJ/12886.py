from collections import deque

def bfs():
    queue = deque([(A, B, C)])
    visited = set([(A, B, C)])

    while queue:
        a, b, c = queue.popleft()
        if a == b == c:
            return 1

        if a != b:
            if a < b and (a+a, b-a, c) not in visited:
                queue.append((a+a, b-a, c))
                visited.add((a+a, b-a, c))
            elif b < a and (a-b, b+b, c) not in visited:
                queue.append((a-b, b+b, c))
                visited.add((a-b, b+b, c))
        
        if a != c:
            if a < c and (a+a, b, c-a) not in visited:
                queue.append((a+a, b, c-a))
                visited.add((a+a, b, c-a))
            elif c < a and (a-c, b, c+c) not in visited:
                queue.append((a-c, b, c+c))
                visited.add((a-c, b, c+c))
        
        if b != c:
            if b < c and (a, b+b, c-b) not in visited:
                queue.append((a, b+b, c-b))
                visited.add((a, b+b, c-b))
            elif c < b and (a, b-c, c+c) not in visited:
                queue.append((a, b-c, c+c))
                visited.add((a, b-c, c+c))
    return 0



A, B, C = map(int, input().split(' '))
print(bfs())