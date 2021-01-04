import sys
sys.setrecursionlimit(10000)

def dfs(node, path, cost):
    global min_cost
    if min_cost < cost: # backtracking!!!!
        return

    if len(path) == N and node == 0:
        min_cost = min(min_cost, cost)
        return

    for w in range(N):
        if graph[node][w] != 0 and w not in path:
            dfs(w, path + [w], cost + graph[node][w])


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split(' '))))

# 1부터 N까지 가는 path를 찾는 문제이므로 DFS!
min_cost = sys.maxsize
dfs(0, [], 0)
print(min_cost)