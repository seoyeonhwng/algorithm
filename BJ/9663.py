N, ans = int(input()), 0
a, b, c = [False] * N, [False] * (2*N-1), [False] * (2*N-1)

def backtracking(i):
    global ans
    if i == N:
        ans += 1
        return
    
    for j in range(N):
        if not (a[j] or b[i+j] or c[i-j+N-1]):
            a[j] = b[i+j] = c[i-j+N-1] = True
            backtracking(i+1)
            a[j] = b[i+j] = c[i-j+N-1] = False

backtracking(0)
print(ans)

# 이차원배열에서 x,y 좌표 합으로 세로, 대각선 두 방향의 위치를 알 수 있음!