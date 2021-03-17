from itertools import combinations
import sys
input = sys.stdin.readline

def get_link():
    link = []
    for i in range(N):
        if i in start:
            continue
        link.append(i)
    return link

N = int(input())
mat = [list(map(int, input().split(' '))) for _ in range(N)]
nums = [i for i in range(N)]
half = N // 2
ans = sys.maxsize

for start in combinations(nums, half):
    s_val = 0
    for i in range(half):
        for j in range(i+1, half):
            a, b = start[i], start[j]
            s_val += mat[a][b] + mat[b][a]

    link, l_val = get_link(), 0
    for i in range(half):
        for j in range(i+1, half):
            a, b = link[i], link[j]
            l_val += mat[a][b] + mat[b][a]

    ans = min(ans, abs(s_val - l_val))
print(ans)


