from collections import defaultdict, deque
import sys


N = int(input())
M = int(input())
graph = defaultdict(list)
back = defaultdict(list)
indegree = [0] * (N+1)

for _ in range(M):
    a, b, t = map(int, input().split(' '))
    graph[a].append((b, t))
    back[b].append((a, t))
    indegree[b] += 1
start, end = map(int, input().split(' '))

# start부터 end까지 최장거리 = 임계경로 -> 위상 정렬을 이용해서 구할 수 있음
result = [0] * (N+1) # 각 노드까지의 최장 거리를 저장
queue = deque([start])
while queue:
    now = queue.popleft()
    for w, wt in graph[now]:
        indegree[w] -= 1
        result[w] = max(result[w], result[now] + wt)
        if indegree[w] == 0:
            queue.append(w)

# 임계경로를 직접 구하기 위해서는 역추적해야함!!
check = [False] * (N+1) # 중복 방문 제거
cnt = 0
queue = deque([end])
while queue:
    now = queue.popleft()
    for w, wt in back[now]:
        if result[now] - result[w] == wt:
            cnt += 1
            if not check[w]:
                queue.append(w)
                check[w] = True
print(result[end])
print(cnt)