N = int(input())

i, j = 1, 1
for cmd in list(input().split(' ')):
    if cmd == 'L': # j-1
        if 1 <= j-1 <= N:
            j -= 1
    elif cmd == 'R': # j+1
        if 1 <= j+1 <= N:
            j += 1
    elif cmd == 'U': # i-1
        if 1 <= i-1 <= N:
            i -= 1
    elif cmd == 'D': # i+1
        if 1 <= i+1 <= N:
            i += 1

print(f'{i} {j}')

"""
# 상하좌우 문제는 dx, dy를 정의하고 이를 이용해서 풀자!
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for cmd in list(input().split(' ')):
    for i, type in enumerate(move_types):
        if cmd == type:
            nx = x + dx[i]
            ny = y + dy[i]
"""