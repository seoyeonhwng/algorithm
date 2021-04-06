N = int(input())
nums = list(map(int, input().split(' ')))

# 내 뒤에 나보다 작은 원소의 연속적인 개수
answer = 0
max_val = 0
count = 0

# 증가하는 부분 수열의 최대 길이 구하기
for n in nums:
    if n > max_val:
        max_val = n
        count = 0
    else:
        count += 1

    answer = max(answer, count)
print(answer)