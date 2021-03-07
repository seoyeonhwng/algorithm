from bisect import bisect_left, bisect_right

N = int(input())
nums = list(map(int, input().split(' ')))

ans = -1
for n in nums:
    s, e = bisect_left(nums, n), bisect_right(nums, n)
    if s <= n < e:
        ans = n
print(ans)