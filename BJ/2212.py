N = int(input())
K = int(input())
nums = list(map(int, input().split(' ')))

# N개의 수를 K개의 구간으로 분할
# K-1개의 간격을 제거 -> 간격이 큰 순으로 제거하자 = 그리디
nums.sort()
diff = []
for i in range(N-1):
    diff.append(nums[i+1] - nums[i])

diff.sort()
for _ in range(K-1):
    if diff:
        diff.pop()
print(sum(diff))

