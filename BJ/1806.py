import sys

N, S = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

# left와 right을 0으로 설정
left = right = s = 0
ans = sys.maxsize

# 누적합이 기준보다 작으면 누적합에 nums[right]를 더하고 right += 1
# 누적합이 기준보다 크거나 같으면 누적합에 nums[left]를 뺴고 left += 1
while True:
    if s >= S:
        ans = min(ans, right - left)
        s -= nums[left]
        left += 1
    else:
        if right == N:
            break
        s += nums[right]
        right += 1
print(0) if ans == sys.maxsize else print(ans)