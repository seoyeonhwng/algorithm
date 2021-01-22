N, K = map(int, input().split(' '))
a_nums = list(map(int, input().split(' ')))
b_nums = list(map(int, input().split(' ')))

# A의 합이 최대 -> K번 A의 최소값과 B의 최대값을 swap
a_nums = sorted(a_nums)
b_nums = sorted(b_nums, reverse=True)

for i in range(K):
    if a_nums[i] < b_nums[i]:
        a_nums[i], b_nums[i] = b_nums[i], a_nums[i]
print(sum(a_nums))