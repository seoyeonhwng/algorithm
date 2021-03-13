import sys
input = sys.stdin.readline

N = int(input())
weights = [int(input()) for _ in range(N)]
weights.sort(reverse=True)

ans = -sys.maxsize
for k in range(N):
    min_w = weights[k] * (k + 1)
    ans = max(ans, min_w)
print(ans)

