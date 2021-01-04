import collections
import sys
sys.setrecursionlimit(100000)

def dfs(node):
    visited.add(node)
    if len(visited) == N: # backtracking
        print(count)
        exit()

    for w in graph[node]:
        if w not in visited:
            dfs(w)
    

N, M = map(int, input().split(' '))
graph = collections.defaultdict(list)

# 요런 종료조건 꼭 넣어주자!
if N == 1:
    print(1)
    exit()
if M == 0:
    print(N)
    exit()

for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

visited, count = set(), 0
for node in range(1, N+1):
    if node not in visited:
        count += 1
        dfs(node)