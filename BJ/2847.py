N = int(input())
level = []
for _ in range(N):
    level.append(int(input()))

answer = 0
for i in range(N-1, 0, -1):
    if level[i] - level[i-1] < 1:
        target = level[i] - 1
        answer += abs(level[i-1] - target)
        level[i-1] = target
print(answer)
