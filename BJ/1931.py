import sys
input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    s, e = map(int, input().split(' '))
    info.append((s, e))
info = sorted(info, key=lambda x: (x[1], x[0]))

# 최대한 회의를 많이 하려면 빨리 끝나는 회의부터 처리 -> 끝나는 시간을 기준으로 정렬
# 만약 끝나는 시간이 같다면 먼저 시작하는 회의부터 처리
ans, time = 1, info[0][1]
for i in range(1, N):
    s, e = info[i]
    if s < time:
        continue

    ans += 1
    time = e
print(ans)