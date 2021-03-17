N, M = map(int, input().split(' '))
data = list(map(int, input().split(' ')))

count = [0] * (M+1)
for d in data:
    count[d] += 1

ans = 0
for i in range(1, M+1):
    N -= count[i]
    ans += count[i] * N
print(ans)