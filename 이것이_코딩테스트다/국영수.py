import sys
input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    s, a, b, c = input().split(' ')
    info.append([s, int(a), int(b), int(c)])

info.sort()
info = sorted(info, key=lambda x : (-x[1], x[2], -x[3]))
for i in info:
    print(i[0])