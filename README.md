*코드 스니펫을 정리합니다.*
## DFS
* path의 특징을 저장해야 할때 사용

  ex) 각 정점에 숫자가 적혀있고 a부터 b까지 가는 경로를 구하는데 경로에 같은 숫자가 있으면 안되는 문제

## BFS (최단 거리)
* 두 노드 사이의 최단 거리 (간선의 개수)를 구할때 사용 -> depth가 최단 거리가 된다!
```
def bfs(start):
  queue = collections.deque([(start, 0)]) # 큐에 (노드, depth)를 저장
  path = set([start])
 
  while queue:
    v, depth = queue.popleft() # deque.popleft는 O(1)
    if v == {종료 조건}:
      return depth
      
    for w in {w가 갈 수 있는 위치}:
      if {w가 유효한 조건 ex.첫방문, 양수}:
        queue.append((w, depth + 1))
        path.add(w)
  retrun -1 # 두 노드 사이의 최단 거리 존재 안함
```

## 다익스트라 (최단 거리)
* 그래프의 한 정점에서 모든 정점까지의 최단 거리를 구할때 사용한다. (크기가 N인 배열을 생각하자!)
  * 힙을 사용하여 최단 거리가 가장 짧은 노드를 선택
```
def dijstra(start):
  heap = [(0, start)]
  dist = [sys.maxsize] * N
  
  while heap:
    cost, now = heapq.heappop(heap)
    if dist[now] < cost: # 이미 최단 거리를 찾은 노드
      continue
    for w, cost_w in graph[now]:
      new_cost = cost + cost_w
      if new_cost < dist[now]:
        dist[now] = new_cost
        heapq.heappush(heap, (new_cost, w))
```

## 플로이드 와샬 (최단 거리)
* 그래프에서 가능한 모든 노드 쌍에 대한 최단 거리를 구할때 사용한다. (N * N matrix를 생각하자!)
```
1. N * N matrix 선언 
  - N = 정점의 개수
  - matrix의 값은 무한대로 채운다.

2. 선언한 matrix에 노드 간의 거리 표시
  - 대각원소는 0으로 채운다.

3. 최단 거리 계산
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]
```

## 크루스칼 (최소 비용 신장 트리)
- 일부 간선만 사용해서 모든 노드가 연결되고, 사이클이 없는 부분 그래프를 만들때 사용한다.
      ex) 도시 사이에 최소한의 비용으로 다리 놓기
```
# 모든 간선을 비용이 작은 순으로 정렬
edges.sort()
for edge in edges:
  cost, a, b = edge
  if find_parent(a) != find_parent(b): # 사이클이 존재하지 않으면 최소 신장 트리에 포함
    union_parent(a, b)
    result += cost
```

## union-find
* 그래프에서 노드들이 같은 집합에 속하는지 검사할때 사용한다.
* 무방향 그래프에서 사이클을 판별할때 사용할 수 있다. (방향 그래프에서는 DFS로 판별)
```
def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]
  
def union_parent(a, b):
  a = find_parent(a)
  b = find_parent(b)
  if a < b:
    parent[a] = b
  else:
    parent[b] = a
```

## 이차원 배열
* 이차원 배열에서 column별로 볼때는 zip을 이용한다.
``` 
A = [[1,2,3], [4,5,6], [7,8,9]]
for col in zip(*A):
    print(col) # (1,4,7) (2,5,8) (3,6,9)
```

* 이차원 배열 모든 원소 합
```
from itertools import chain

A = [[1,2,3], [4,5,6], [7,8,9]]
total_sum = sum(chain(*A)) # chain은 리스트를 연결해줌
```


* 이차원 배열 탐색
```
di = [0, 1, 2, 3] # 'up', 'right', 'down', 'left'
di = (di - 1) % 4 # 왼쪽 회전
di = (di + 1) % 4 # 오른쪽 회전

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
(x, y) -> (x + dx[di], y + dy[di])로 이동
```

## counter
* 값이 0이하인 원소 없애기
```
counter += collections.Counter() # 빈 counter를 더한다
```

## 기타
* 단조 감소 배열인지 확인
```
all(x>=y for x, y in zip(L, L[1:]))
```

* 배열 회전 (deque를 이용하는 방법이 slicing보다 빠름)
```
from collections import deque

queue = deque([1,2,3])
queue.rotate(1) # [3, 1, 2]
```

