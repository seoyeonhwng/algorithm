from collections import deque

def get_new_number(n):
    n = n * 2
    head = int(str(n)[0]) - 1
    rest = str(n)[1:]
    return int(str(head) + rest)
    
def bfs():
    queue = deque([(N, T)])
    visited = set([N])

    while queue:
        n, count = queue.popleft()

        if count < 0:
            return 'ANG'
        if n == G:
            return T - count
        
        # 버튼 A
        if n + 1 <= 99999 and (n + 1) not in visited:
            queue.append((n+1, count-1))
            visited.add(n+1)
        
        # 버튼 B
        if n == 0 or n * 2 > 99999:
            continue

        nn = get_new_number(n)
        if nn not in visited:
            queue.append((nn, count-1))
            visited.add(nn)
    return 'ANG'

N, T, G = map(int, input().split(' '))

# N부터 G까지 최단 거리 -> BFS !!
print(bfs())