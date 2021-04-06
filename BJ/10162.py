T = int(input())

answer = []
for unit in [300, 60, 10]:
    q, r = divmod(T, unit)
    answer.append(q)
    T = r

if T != 0:
    print(-1)
else:
    print(*answer)