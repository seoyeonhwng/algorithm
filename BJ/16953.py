from collections import deque

def bfs():
    queue = deque([(0, A)])
    visited = set([A])

    while queue:
        count, num = queue.popleft()
        if num == B:
            return count
        
        for w in [num * 2, int(str(num) + '1')]:
            if w < 1 or w > 1000000000:
                continue
            if w in visited:
                continue
            queue.append((count + 1, w))
            visited.add(w) 
    return -2

A, B = map(int, input().split(' '))

# A에서 B로 최단 거리 이동 -> bfs!!
print(bfs() + 1)