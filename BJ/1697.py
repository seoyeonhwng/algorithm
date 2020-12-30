# 두 노드 사이의 최단 거리 -> BFS
# depth를 구할때 node w의 depth는 v의 depth + 1로 저장하면서 구하자!

import collections

def bfs(start, check):
    queue = collections.deque([start])
  
    while queue:
        v = queue.popleft()
        if v == K:
            return check[v]

        for w in [v-1, v+1, 2*v]:
            if (0 <= w <= 100000) and check[w] == 0:
                check[w] = check[v] + 1
                queue.append(w)


N, K = map(int, input().split(' '))
check = [0] * 1000001
print(bfs(N, check))