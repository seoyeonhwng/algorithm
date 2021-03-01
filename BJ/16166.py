from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def bfs():
    ans = sys.maxsize

    while queue:
        line, node, count = queue.popleft()

        if node == E:
            ans = min(ans, count)
            continue

        for w_line, w in graph[(line, node)]:
            if (w_line, w) in visited:
                continue
            queue.append((w_line, w, count))
            visited.add((w_line, w))

        for new_line in transfer[node]:
            if new_line == line:
                continue
            if (new_line, node) in visited:
                continue
            queue.append((new_line, node, count + 1))
            visited.add((new_line, node))

    return ans
        

N = int(input())
graph = defaultdict(list)
transfer = defaultdict(list)

queue = deque()
visited = set()

for i in range(N):
    info = deque(list(map(int, input().split(' '))))
    k = info.popleft()

    if 0 in info:
        queue.append((i, 0, 0))
        visited.add((i, 0))

    for j in range(k-1):
        a, b = (i, info[j]), (i, info[j+1])
        graph[a].append(b)
        graph[b].append(a)
        transfer[info[j]].append(i)
    transfer[info[-1]].append(i)
E = int(input())

ans = bfs()
print(-1) if ans == sys.maxsize else print(ans)