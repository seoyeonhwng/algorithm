from bisect import bisect_left, bisect_right

N, X = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

ans = bisect_right(nums, X) - bisect_left(nums, X)
print(-1) if ans == 0 else print(ans)