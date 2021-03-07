import sys
input = sys.stdin.readline

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
# 간선을 N-1개 만들어서 모든 노드 연결 -> 크루스칼!
N = int(input())
x, y, z = [], [], []
for i in range(N):
    a, b, c = map(int, input().split(' '))
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(N-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

# 간선 비용 순으로 정렬
edges.sort()

parent = [i for i in range(N)]
ans = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += cost
print(ans)

"""
* 해설
- 모든 두 행성 간의 거리를 확인하는 방법 -> 메모리 초과
- 행성간의 x축, y축, z축 간의 거리로 정의 (어렵다..)
"""