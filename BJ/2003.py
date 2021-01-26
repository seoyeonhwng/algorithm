N, M = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

# left, ans = 0, 0
# while left < N:
#     right = left
#     # expand right
#     total = 0
#     while total < M and right < N:
#         total += nums[right]
#         right += 1
    
#     if total == M:
#         ans += 1
#     left += 1
# print(ans)
        
left = right = ans = s = 0
while True:
    if s >= M:
        s -= nums[left]
        left += 1
    else:
        if right == N:
            break
        s += nums[right]
        right += 1
    
    if s == M:
        ans += 1
print(ans)