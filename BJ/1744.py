import sys
input = sys.stdin.readline

N = int(input())

pos, neg, one = [], [], []
for _ in range(N):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num == 1:
        one.append(num)
    else:
        neg.append(num)

# 1이면 무조건 더하기
ans = sum(one)
pos.sort(reverse=True)
p_len = len(pos)

# 1보다 큰 양수들은 정렬 후 짝지어서 더하기
for i in range(0, p_len, 2):
    if i + 1 < p_len:
        ans += pos[i] * pos[i+1]
    else:
        ans += pos[i]

# 0보다 같거나 작은 수들은 정렬 후 짝지어서 더하기
neg.sort()
n_len = len(neg)
for i in range(0, n_len, 2):
    if i + 1 < n_len:
        ans += neg[i] * neg[i+1]
    else:
        ans += neg[i]
print(ans)