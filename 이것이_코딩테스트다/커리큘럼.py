from collections import defaultdict, deque

N = int(input())
time = [0] * (N+1)
graph = defaultdict(list)
indegree = defaultdict(int)

for i in range(1, N+1):
    infos = list(map(int, input().split(' ')))
    time[i] = infos[0]
    for info in infos[1:-1]:
        graph[info].append(i)
        indegree[i] += 1

result = [0] * (N+1) # 각 노드마다 최장거리 저장
queue = deque()

# indegree가 0인 노드를 큐에 삽입
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        result[i] = time[i]

while queue:
    now = queue.popleft()
    for w in graph[now]:
        indegree[w] -= 1
        result[w] = max(result[w], time[w] + result[now])
        if indegree[w] == 0:
            queue.append(w)

for r in result[1:]:
    print(r)

# 위상정렬을 사용해서 노드의 최장 거리(임계거리, critical path)를 구할 수 있음!