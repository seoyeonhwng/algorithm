def convert(n, m):
    # (i, j)부터 시작해서 3*3크기의 A의 부분행렬값을 뒤집음
    for i in range(n, n+3):
        for j in range(m, m+3):
            matA[i][j] = 1 if matA[i][j] == 0 else 0


def check():
    for i in range(N):
        for j in range(M):
            if matA[i][j] != matB[i][j]:
                return False
    return True

N, M = map(int, input().split(' '))
matA = [list(map(int, list(input()))) for _ in range(N)]
matB = [list(map(int, list(input()))) for _ in range(N)]

# 앞에서부터 하나씩 A와 B가 다르면 뒤집기 연산 수행
ans = 0
for i in range(N-2):
    for j in range(M-2):
        if matA[i][j] != matB[i][j]:
            convert(i, j)
            ans += 1

print(-1) if not check() else print(ans)