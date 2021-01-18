from collections import defaultdict

A, P = map(int, input().split(' '))
array, n = defaultdict(int), A

while True:
    array[n] += 1
    if array[n] == 3:
        break

    # n의 각 자리 수를 P번 곱해서 더한다
    total = 0
    for s in str(n):
        total += int(s) ** P
    n = total

ans = 0
for v in array.values():
    if v == 1: ans += 1
print(ans)