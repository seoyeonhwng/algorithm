N = int(input())
seats = input()

cups, i = '*', 0
while i < N:
    if seats[i] == 'S':
        cups += 'S'
        i += 1
    else:
        cups += 'LL'
        i += 2
    cups += '*'

M = len(cups)
check = [False] * M
answer = 0

# 왼쪽에서부터 최대한 컵홀더를 나눠줌 -> 그리디
for i in range(M):
    if cups[i] == '*':
        continue

    if not check[i-1] and cups[i-1] == '*':
        check[i-1] = True
        answer += 1
    elif not check[i+1] and cups[i+1] == '*':
        check[i+1] = True
        answer += 1
print(answer)

