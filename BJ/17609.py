def check(left, right):
    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

for _ in range(int(input())):
    s = input()
    N = len(s)

    left, right, ans = 0, N-1, 0
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else: # 회문이 아님 -> 유사 회문인지 판단
            l = check(left + 1, right)
            r = check(left, right - 1)
            if l or r:
                ans = 1
            else:
                ans = 2
            break
    
    print(ans)

# left, right = 0, N-1에서 시작해서 한칸씩 이동
# s[left] == s[right]라면 pass
# 다르다면 유사 회문인지 체크 -> left를 이동한 문자열과 right을 이동한 문자열 각각에 대해서 회문인지 검사
# 둘중 하나라도 회문이면 유사회문 아니면 아무것도 아님