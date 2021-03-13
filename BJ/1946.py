import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    info = [list(map(int, input().split(' '))) for _ in range(N)]

    info.sort()
    ans, min_rank = 1, info[0][1]
    for i in range(1, N):
        if info[i][1] < min_rank:
            ans += 1
        min_rank = min(min_rank, info[i][1])
    print(ans)