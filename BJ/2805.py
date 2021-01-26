def binary_search(start, end):
    global ans

    while start <= end:
        mid = (start + end) // 2

        # mid로 나무를 자르자
        check = sum([h - mid for h in heights if h >= mid])
        if check >= M:
            start = mid + 1
            ans = max(ans, mid)
        else:
            end = mid - 1
    

N, M = map(int, input().split(' '))
heights = list(map(int, input().split(' ')))

start, end = 0, max(heights)
ans = 0
binary_search(start, end)
print(ans)