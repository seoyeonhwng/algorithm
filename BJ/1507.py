N = int(input())
mat = []
connect = [[1] * N for _ in range(N)]

for _ in range(N):
    mat.append(list(map(int,input().split(' '))))

valid = True
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or i == k or k == j:
                continue

            # 거쳐가는 경우 삭제 (연결 여부는 connect으로 관리)
            if mat[i][j] == mat[i][k] + mat[k][j]:
                connect[i][j] = 0
            elif mat[i][j] > mat[i][k] + mat[k][j]:
                valid = False

if not valid:
    print('-1')
else:  
    answer = 0   
    for i in range(N):
        for j in range(i+1, N):
            answer += mat[i][j] if connect[i][j] else 0
    print(answer)