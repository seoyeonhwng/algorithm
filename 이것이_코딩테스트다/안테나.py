N = int(input())
nums = list(map(int, input().split(' ')))
nums.sort()

idx = N // 2 - 1 if N % 2 == 0 else N // 2
print(nums[idx])

