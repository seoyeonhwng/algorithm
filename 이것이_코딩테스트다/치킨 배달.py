from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

def get_dist(chicken, home):
    # M개의 치킨집이 주어졌을때 모든 집의 치킨 거리의 합을 구함 (bfs로 구할 필요가 없음)
    dist = 0
    for x, y in home:
        tmp = sys.maxsize
        for cx, cy in chicken:
            tmp = min(tmp, abs(cx - x) + abs(cy - y))
        dist += tmp
    return dist


N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

home, chicken = [], []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            home.append((i, j))
        elif mat[i][j] == 2:
            chicken.append((i, j))

# 모든 경우에 대해 완전 탐색
ans = sys.maxsize
for candi in combinations(chicken, M):
    ans = min(ans, get_dist(candi, home))
print(ans)