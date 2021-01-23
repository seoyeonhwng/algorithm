import sys

def binary_search(heights, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2

        # mid로 떡을 잘랐을때 값이 target이면 return
        cut = sum([h - mid for h in heights if h > mid])

        if cut < target: # target보다 덜 자른 경우 높이 감소
            end = mid - 1
        else:
            result = max(result, mid) # 최대 높이
            start = mid + 1

    return result

        

N, M = map(int, input().split(' '))
heights = list(map(int, sys.stdin.readline().rstrip().split(' ')))

heights.sort()
print(binary_search(heights, M, 0, heights[-1]))