from collections import deque

N, L = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

queue = deque()
ans = []
for i, n in enumerate(nums):
    if not queue:
        queue.append((n, i))
    else:
        if i - queue[0][1] >= L: # index 넘어간 경우 
            queue.popleft()

        while queue and queue[-1][0] > n: # n보다 큰 수는 다 pop
            queue.pop()
        queue.append((n, i))

    # 큐 맨 앞의 값 = 최솟값
    ans.append(queue[0][0])
print(*ans)