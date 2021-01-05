from collections import deque

def is_valid(a, b):
    if a < 0 or a >= N or b < 0 or b >= M:
        return False
    if box[a][b] != 0: # 0인 애들만 bfs의 대상!
        return False
    return True

def bfs(queue):
    while queue:
        a, b = queue.popleft()

        for new_a, new_b in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
            if is_valid(new_a, new_b):
                box[new_a][new_b] = box[a][b] + 1
                queue.append((new_a, new_b))


M, N = map(int, input().split(' '))
box = []
for _ in range(N):
    box.append(list(map(int, input().split(' '))))

# 1인곳을 다 큐에 넣고 bfs!
# bfs의 depth를 기록 -> max가 답!
queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

bfs(queue)
ans = 1
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans, box[i][j])
print(ans-1)
