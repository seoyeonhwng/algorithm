from collections import deque

def bfs():
    queue = deque([(N, 0)])
    visited = set([N])
    prev = {N: -1}

    while queue:
        num, count = queue.popleft()
        if num == K:
            return count, prev

        for w in [num+1, num-1, num*2]:
            if (w < 0) or (w > 100000) or (w in visited):
                continue
            queue.append((w, count + 1))
            visited.add(w)
            prev[w] = num


N, K = map(int, input().split(' '))
count, prev = bfs()

path, cur = deque([K]), K
while True:
    p = prev[cur]
    if p == -1:
        break
    path.appendleft(p)
    cur = p
print(count)
print(*path)

# 최단경로 저장할때 엄청 큼!! -> 이전 값만 저장하는 식으로 해결