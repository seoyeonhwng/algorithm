# dfs로 로봇을 이동
# N == 0이면 리턴 이때 중복된 path가 있으면 해당 확률을 정답에 더함!

def dfs(x, y, n, p, path):
    global ans
    if n == 0:
        if len(set(path)) == N+1:
            ans += p
        return
        
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (nx, ny) not in path:
            path.append((nx, ny))
            dfs(nx, ny, n-1, p * prob[i], path)
            path.pop()

    
N, ep, wp, sp, np = map(int, input().split(' '))

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
prob = [ep/100, wp/100, sp/100, np/100]

ans = 0
dfs(0, 0, N, 1, [(0, 0)])
print(ans)