import sys

def move_left(b, s, e):
    # 왼쪽으로 움직여서 포함되도록
    count = 0
    while s >= 0:
        if s <= b < e:
            return count
        s, e = s - 1, e - 1
        count += 1
    return sys.maxsize

def move_right(b, s, e):
    # 오른쪽으로 움직여서 포함되도록
    count = 0
    while e <= N:
        if s <= b < e:
            return count
        s, e = s + 1, e + 1
        count += 1
    return sys.maxsize


N, M = map(int, input().split(' '))
J = int(input())
balls = [int(input()) for _ in range(J)]

s, e = 0, M # s <= x < e
answer = 0
for b in balls:
    left = move_left(b-1, s, e)
    right = move_right(b-1, s, e)

    # 둘 중 더 작은 쪽으로 이동 -> 그리디 !!
    step = -left if left < right else right
    s, e = s + step, e + step
    answer += abs(step)
print(answer)

