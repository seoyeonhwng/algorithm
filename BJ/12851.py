from collections import deque, defaultdict
import sys

def bfs():
    queue = deque([N])
    check = [-1 for _ in range(100001)] # N에서부터 index까지 최단 거리를 저장
    check[N] = 0
    ans = 0

    while queue:
        num = queue.popleft()
        if num == K:
            ans += 1
            continue

        for w in [num-1, num+1, num*2]:
            if w < 0 or w > 100000:
                continue
            if check[w] == -1 or check[w] == check[num] + 1:
                check[w] = check[num] + 1
                queue.append(w)

    return (check[K], ans)

    
# N에서 K까지 최단 이동 시간 -> bfs!!
N, K = map(int, input().split(' '))
dist, count = bfs()
print(dist)
print(count)

"""
최단 경로의 개수를 구하는 경우
- queue에 count를 넣지말고 각 노드까지의 최단 거리를 저장하는 배열 선언
- queue에 노드를 넣을때 첫방문이거나 최단 거리랑 같은 경우만 삽입
"""