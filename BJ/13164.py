# N명을 K개의 조로 나눈다 (비용이 적게 들도록)
N, K = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

nums.sort()
diff = []
for i in range(N-1):
    diff.append(nums[i+1] - nums[i])

diff.sort()
for _ in range(K-1):
    if diff:
        diff.pop()
print(sum(diff))