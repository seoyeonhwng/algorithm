import sys

N = int(input())
ans = 0

while N >= 0:
    # 5로 많이 나눠야 최적의 해 -> 5로 나눠질떄까지 3씩 빼줌
    if N % 5 == 0:
        print(ans + N // 5)
        break

    N -= 3
    ans += 1
else:
    print(-1)