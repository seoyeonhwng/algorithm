def dfs(num):
    if num in visited or num > N:
        return
    
    visited.add(num)
    for w in [4, 7]:
        dfs(num*10 + w)

N = int(input())
visited = set()
dfs(0)
print(max(visited))