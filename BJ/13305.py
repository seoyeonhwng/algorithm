# 나보다 주유소 값이 싼 곳을 만날때까지 전진
N = int(input())
roads = list(map(int, input().split(' ')))
stations = list(map(int, input().split(' ')))

ans = 0
s, r = stations[0], roads[0]
for i in range(1, N-1):
    if s <= stations[i]:
        r += roads[i]
    else:
        ans += s * r
        s, r = stations[i], roads[i]
ans += s * r
print(ans)