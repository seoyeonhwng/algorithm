nums = []
for _ in range(int(input())):
    nums.append(int(input()))

print(*sorted(nums, reverse=True))