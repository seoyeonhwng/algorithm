from math import sqrt
import sys
input = sys.stdin.readline

def get_dist(i, j):
    x1, y1 = position[i]
    x2, y2 = position[j]

    ans = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return sqrt(ans)

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


N, M = map(int, input().split(' '))
position = {}
for i in range(1, N+1):
    x, y = map(int, input().split(' '))
    position[i] = (x, y)

edges = []
for _ in range(M):
    a, b = map(int, input().split(' '))
    edges.append((0, a, b))

for i in range(1, N+1):
    for j in range(i+1, N+1):
        dist = get_dist(i, j)
        edges.append((dist, i, j))

edges.sort()
ans = 0
parent = [i for i in range(N+1)]

for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += cost
print(format(ans, '.2f'))
