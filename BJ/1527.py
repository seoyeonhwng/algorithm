def dfs(n):
    if n in visited or n > B:
        return
  
    visited.add(n)
    for w in [4, 7]:
        dfs(n * 10 + w)

A, B = map(int, input().split(' '))

visited = set()
dfs(0)

ans = len(visited)
for i, v in enumerate(visited):
    if v < A:
        ans -= 1
print(ans)