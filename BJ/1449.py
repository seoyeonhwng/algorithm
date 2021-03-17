N, L = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

# 앞에서부터 하나씩 L-1이 될때까지 테이프를 붙임
nums.sort()
left, right, ans = 0, 0, 0
while left < N:
    while right < N and nums[right] - nums[left] <= L-1:
        right += 1
    
    left, right = right, left + 1
    ans += 1
print(ans)
