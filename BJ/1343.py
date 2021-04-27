def get_string(left, right):
    A_count, r = divmod(right - left, 4)
    B_count, r = divmod(r, 2)
    
    if r != 0:
        return -1
    return 'AAAA' * A_count + 'BB' * B_count

s = input()
N, left = len(s), 0

# 사전순으로 가장 앞서는 답 -> A를 최대한 배치
answer = ''
while left < N:
    if s[left] == '.':
        left += 1
        answer += '.'
        continue

    right = left
    while right < N and s[right] == 'X':
        right += 1
    
    new_str = get_string(left, right)
    if new_str == -1:
        answer = -1
        break

    answer += new_str
    left = right
print(answer)