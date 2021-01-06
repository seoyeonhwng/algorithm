N, M = map(int, input().split(' '))
cards = [list(map(int, input().split(' '))) for _ in range(N)]

# 각 row의 min 중에서 max를 고른다!!
ans = 0
for row in cards:
    min_row = min(row)
    ans = max(ans, min_row)
print(ans)