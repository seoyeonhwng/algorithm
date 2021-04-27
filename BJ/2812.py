import heapq

N, K = map(int, input().split(' '))
nums = list(map(int, list(input())))

# 가장 큰 수를 만들기 위해서는 큰 숫자가 앞에 와야함
# nums[i]를 배치하기 전에 nums[i]보다 작은 숫자는 pop
stack, count = [], 0
for i in range(N):
    while stack and stack[-1] < nums[i] and count < K:
        stack.pop()
        count += 1
    stack.append(nums[i])

# 그래도 K가 남았다면 (내림차순이라는 뜻) 뒤에서 부터 삭제
while stack and count < K:
    stack.pop()
    count += 1

answer = ''
for s in stack:
    answer = answer + str(s)
print(answer)


