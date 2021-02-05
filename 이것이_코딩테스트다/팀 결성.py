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


# 팀 합치기, 같은 팀 여부 확인 -> union-find
N, M = map(int, input().split(' '))

# 부모 노드를 저장하는 배열 및 초기화
parent = [0] * (N + 1)
for i in range(N+1):
    parent[i] = i

for _ in range(M):
    op, a, b = map(int, input().split(' '))
    if op == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
