import sys

N = int(input())
mat = [[sys.maxsize] * N for _ in range(N)]

while True:
    a, b = map(int, input().split(' '))
    if a == -1 and b == -1:
        break
    mat[a-1][b-1] = 1
    mat[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if mat[i][j] > mat[i][k] + mat[k][j]:
                mat[i][j] = mat[i][k] + mat[k][j]

for i in range(N):
    for j in range(N):
        if mat[i][j] == sys.maxsize:
            mat[i][j] = 0

info = {}
for i, row in enumerate(mat):
    info[i] = max(row)

winner_score, winners = min(info.values()), []
for k, v in info.items():
    if v == winner_score:
        winners.append(k)

print(f'{winner_score} {len(winners)}')
print(' '.join([str(w + 1) for w in winners]))