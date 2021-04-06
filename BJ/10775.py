import sys
sys.setrecursionlimit(1000000)

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


G = int(input())
gates = []
for _ in range(int(input())):
    gates.append(int(input()))

# 가능한 가장 번호가 큰 게이트에 도킹 -> 그리디
# parent에 가능한 게이트를 저장 -> union-find
parent = [i for i in range(G+1)]
answer = 0
for g in gates:
    idx = find_parent(g)
    if idx == 0:
        break

    union_parent(g, idx-1)
    answer += 1
print(answer)