from collections import defaultdict
def dfs(node, target):
    print('++', node, target)
    if node != target[0]:
        return False
    
    for w in graph[node]:
        if visited[w]:
            continue

        visited[w] = True
        tmp = target.pop(0)
        if not dfs(w, target[1:]):
            return False
        target.append(tmp)
        
    return True
    

N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
target = list(map(int, input().split(' ')))

visited = [False] * (N+1)
visited[1] = True
result = dfs(1, target)
print(result)