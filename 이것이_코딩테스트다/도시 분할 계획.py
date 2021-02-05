# 마을을 2개로 분리! 길의 유지비 합을 최소
# 크루스칼 알고리즘으로 최소 신장 트리를 구하고 그 중에서 유지비 합이 가장 큰 간선을 삭제
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split(' '))
edges = []
for _ in range(M):
    a, b, c = map(int, input().split(' '))
    edges.append((c, a, b))

# 전체 간선 정렬
edges.sort()

# 부모 노드 배열 초기화
parent = [0] * (N+1)
for i in range(N+1):
    parent[i] = i

ans = []
for c, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans.append(c)

print(sum(ans) - max(ans))

"""
- 간선을 정렬한 상태이므로 ans에 들어가는 마지막 간선이 최대값!
for c, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += c
        last = c
print(result - last)
"""