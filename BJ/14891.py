from collections import defaultdict, deque

def do_rotation(num, d):
    # 해당 톱니바퀴를 d가 1이면 시계, -1이면 시계 반대방향으로 회전

    candi = [(num, d)]
    right, right_d = num + 1, -d
    while right < 5:
        if cycles[right][-2] != cycles[right-1][2]:
            candi.append((right, right_d))
            right_d = -right_d
            right += 1
        else:
            break
    
    left, left_d = num - 1, -d
    while left >= 1:
        if cycles[left][2] != cycles[left + 1][-2]:
            candi.append((left, left_d))
            left_d = -left_d
            left -= 1
        else:
            break

    for n, di in candi:
        cycles[n].rotate(di)


cycles = defaultdict(list)
for i in range(1, 5):
    cycles[i] = deque(list(map(int, list(input()))))

for _ in range(int(input())):
    num, d = map(int, input().split(' '))
    do_rotation(num, d)

answer = 0
for i in range(1, 5):
    if cycles[i][0] == 1:
        answer += 2 ** (i-1)
print(answer)