def dfs(mat, i, j, target):
    # 종료 조건 (땅이 아님)
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
        return
    
    if mat[i][j] == target:
        return
    
    mat[i][j] = target
    # 동서남북 탐색
    dfs(mat, i+1, j, target)
    dfs(mat, i-1, j, target)
    dfs(mat, i, j+1, target)
    dfs(mat, i, j-1, target)

    

M, N = input().split(' ')
mat1, mat2 = [], []
for i in range(int(M)):
    tmp = list(input().replace(' ', ''))
    mat1.append(tmp[:])
    mat2.append(tmp[:])


# 0 -> 1 : 0이면 dfs
zero_one = 0
for i in range(int(M)):
    for j in range(int(N)):
        if mat1[i][j] == '0':
            dfs(mat1[:], i, j, '1')
            zero_one += 1

# 1 -> 0 : 1이면 dfs
one_zero = 0
for i in range(int(M)):
    for j in range(int(N)):
        if mat2[i][j] == '1':
            dfs(mat2, i, j, '0')
            one_zero += 1

print(zero_one, one_zero)