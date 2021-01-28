import sys

N = int(input())
mat = [[sys.maxsize] * N for _ in range(N)]
for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    mat[a-1][b-1] = 1
    mat[b-1][a-1] = 1

for i in range(N):
    mat[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if mat[i][j] > mat[i][k] + mat[k][j]:
                mat[i][j] = mat[i][k] + mat[k][j]

max_info = {}
groups = []
for i in range(N):
    max_info[i] = max([mat[i][j] for j in range(N) if mat[i][j] != sys.maxsize])
    group = [j for j in range(N) if mat[i][j] != sys.maxsize]
    if group not in groups:
        groups.append(group)

print(len(groups))
ans = []
for group in groups:
    leader, leader_val = sys.maxsize, sys.maxsize
    for g in group: # group에서 최솟값 찾기
        if max_info[g] < leader_val:
            leader, leader_val = g, max_info[g]
    ans.append(leader + 1)
print(*sorted(ans), sep='\n')
