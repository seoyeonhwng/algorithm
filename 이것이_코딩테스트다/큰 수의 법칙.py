N, M, K = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
nums.sort()

first = nums.pop()
second = nums.pop()
total = 0

while M > 0:
    # first를 K만큼 더하고 second를 한번 더함
    total += first * K + second
    M -= (K + 1)
print(total)
    
"""
# first, second를 구할때 굳이 pop하지 않고 index로 접근하자!
fisrt = nums[-1]
second = nums[-2]

# 'first K번 후 second 1번' 꼴의 수열이 계속 반복되는 형태 
# q, r = divmod(M, K+1)
    - q는 수열이 반복되는 횟수
    - 가장 큰 수가 반복되는 횟수는 q * K + r
    - 두번째로 큰 수가 반복되는 횟수는 M - (가장 큰 수가 반복되는 횟수)
"""