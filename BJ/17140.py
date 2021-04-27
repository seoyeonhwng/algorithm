from collections import Counter, defaultdict

def get_new_arr(arr):
    if len(arr) > 100:
        arr = arr[:100]

    counts = defaultdict(int)
    for a in arr:
        if a > 0:
            counts[a] += 1

    new_arr = []
    for k, v in sorted(counts.items(), key=lambda x:(x[1], x[0])):
        new_arr += [k, v]
    return new_arr

def do_R(mat):
    # 모든 행에 대해서 정렬을 수행
    # 각 행마다 등장횟수를 셈
    # 등장횟수가 큰 순으로, 같다면 수가 커지는 순
    # 가장 큰 행을 기준으로 맞추고 작다면 0으로 패딩
    tmp = []
    for row in mat:
        arr = get_new_arr(row)
        tmp.append(arr)

    max_len = max(tmp, key=len)
    max_len = len(max_len)

    new_mat = []
    for t in tmp:
        new_row = t + [0] * (max_len - len(t))
        new_mat.append(new_row)

    return new_mat

def do_C(mat):
    tmp = []
    for col in zip(*mat):
        arr = get_new_arr(col)
        tmp.append(arr)
    
    max_len = max(tmp, key=len)
    max_len = len(max_len)

    r_new_mat = []
    for t in tmp:
        new_row = t + [0] * (max_len - len(t))
        r_new_mat.append(new_row)
    
    new_mat = []
    for row in zip(*r_new_mat):
        new_mat.append(list(row))

    return new_mat


R, C, K = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(3)]

answer = 0
while True:
    N, M = len(mat), len(mat[0])
    if 0 <= R-1 < N and 0 <= C-1 < M and mat[R-1][C-1] == K:
        break
    if answer > 100:
        break

    if N >= M:
        mat = do_R(mat)
    else:
        mat = do_C(mat)
    answer += 1

print(-1) if answer > 100 else print(answer)