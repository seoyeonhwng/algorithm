S = list(input())
N = len(S)

left, right = 0, 1
zero, one = 0, 0

while left < right and right <= N:
    
    while right < N and S[left] == S[right]:
        right += 1

    if S[left] == '0':
        zero += 1
    else:
        one += 1
    
    left, right = right, right + 1

print(min(one, zero))
