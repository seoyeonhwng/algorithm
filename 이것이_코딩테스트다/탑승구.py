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

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]
ans = 0
for _ in range(P):
    plane = int(input())
    # 현재 비행기의 탑승구 루트를 확인
    root = find_parent(plane)
    if root == 0:
        break
    # 0이 아니면 왼쪽 집합과 합침
    union_parent(root, root-1)
    ans += 1
print(ans)

