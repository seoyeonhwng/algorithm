import sys

N, R = map(int, input().split(' '))
total_cities = list(set(input().split(' ')))
M = int(input())
travel = list(input().split(' '))
K = int(input())

# total_cities를 기준으로 maps를 채운다!
maps = [[sys.maxsize] * N for _ in range(N)]
tommorows = [[sys.maxsize] * N for _ in range(N)]
city_idx_map = {c : i for i, c in enumerate(total_cities)}

for _ in range(K):
    t, s, e, c = input().split(' ')
    s_idx, e_idx = city_idx_map[s], city_idx_map[e]
    maps[s_idx][e_idx] = min(maps[s_idx][e_idx], int(c))
    maps[e_idx][s_idx] = min(maps[e_idx][s_idx], int(c))
    
    if t in ['Mugunghwa', 'ITX-Saemaeul', 'ITX-Cheongchun']:
        tommorows[s_idx][e_idx] = min(tommorows[s_idx][e_idx], 0)
        tommorows[e_idx][s_idx] = min(tommorows[e_idx][s_idx], 0)
    elif t in ['S-Train', 'V-Train']:
        tommorows[s_idx][e_idx] = min(tommorows[s_idx][e_idx], int(c) // 2 + 1) # 비용이기 때문에 올림처리!
        tommorows[e_idx][s_idx] = min(tommorows[e_idx][s_idx], int(c) // 2 + 1)
    else:
        tommorows[s_idx][e_idx] = min(tommorows[s_idx][e_idx], int(c))
        tommorows[e_idx][s_idx] = min(tommorows[e_idx][s_idx], int(c))
        
for i in range(N):
    maps[i][i] = 0
    tommorows[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if maps[i][j] > maps[i][k] + maps[k][j]:
                maps[i][j] = maps[i][k] + maps[k][j]
            if tommorows[i][j] > tommorows[i][k] + tommorows[k][j]:
                tommorows[i][j] = tommorows[i][k] + tommorows[k][j]

# travel을 보면서 하나씩 값을 계산
total, tommorows_total = 0, 0
for i in range(M-1):
    a, b = city_idx_map[travel[i]], city_idx_map[travel[i+1]]
    total += maps[a][b]
    tommorows_total += tommorows[a][b]

print('Yes') if tommorows_total + R < total else print('No')