import re

N = int(input())
for _ in range(N):
    string = input()
    if re.fullmatch('(100+1+|01)+', string):
        print('YES')
    else:
        print('NO')
