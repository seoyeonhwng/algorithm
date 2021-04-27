from collections import defaultdict, deque
import sys
from itertools import combinations

def bfs(combi):
    queue = deque([combi[0]])
    visited = set([combi[0]])
    s = 0

    while queue:
        node = queue.popleft()
        s += nums[node-1]

        for w in graph[node]:
            if (w not in visited) and (w in combi):
                queue.append(w)
                visited.add(w)

    return len(visited), s 


N = int(input())
nums = list(map(int, input().split(' ')))

graph = defaultdict(list)
for i in range(1, N+1):
    tmp = list(map(int, input().split(' ')))
    graph[i] = tmp[1:]

answer = sys.maxsize
for i in range(1, N//2+1):
    # nums에서 i개수만큼 조합 생성
    for combi in list(combinations([i for i in range(1, N+1)], i)):
        A = list(combi)
        B = [n for n in range(1, N+1) if n not in A]

        # A에 대해서 dfs
        c1, s1 = bfs(A)
        # B에 대해서 dfs
        c2, s2 = bfs(B)
#         # 각각 도달한 원소의 합이 N이면 answer 갱신
        if c1 + c2 == N:
            answer = min(answer, abs(s1 - s2))
print(-1) if answer == sys.maxsize else print(answer)