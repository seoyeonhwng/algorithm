N, K = map(int, input().split(' '))

count = 0
while N > 1:
    # 최소 횟수이므로 K로 나누는 것을 먼저!
    if N % K == 0:
        N = N // K
    else:
        N -= 1
    count += 1
print(count)

"""
일일이 1씩 빼지 않고 N이 K의 배수가 되도록 효율적으로 한번에 빼자!
- N이 K가 되도록 한다
- N을 K로 나눈다
- 위 과정을 N == 1일때까지 반복한다

while True:
    # N보다 작은 수 중에서 가장 큰 K의 배수
    target = (N // K) * K
    result = (n - target) # 1을 뺀 횟수
    N = target

    if N < K:
        break
    result += 1
    N //= K

# 남은 수 1씩 뺘가
result += (N - 1)
"""
