from collections import defaultdict

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# A, B 부배열 가능한 값을 구함
subA = defaultdict(int)
for i in range(N):
    s = 0
    for j in range(i, N):
        s += A[j]
        subA[s] += 1

subB = defaultdict(int)
for i in range(M):
    s = 0
    for j in range(i, M):
        s += B[j]
        subB[s] += 1

# A의 paritial sum을 돌면서 필요한 값이 B의 partial sum에 있는지 체크
ans = 0
for value, count in subA.items():
    if subB.get(T-value, 0):
        ans += count * subB[T-value]
print(ans)