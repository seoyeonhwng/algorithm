N = int(input())
matrix = [input().split(' ') for _ in range(N)]

# 모든 정점에 대한 최단거리이므로 플로이드 와샬
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][k] == '1' and matrix[k][j] == '1':
                matrix[i][j] = '1'

for row in matrix:
    print(' '.join([r for r in row]))