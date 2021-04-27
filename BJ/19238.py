from collections import deque
import heapq

def find_nearest_customer(tx, ty):
    # 현재 택시 위치 (tx, ty)에서 가장 가까운 손님 찾기
    queue = deque([(tx, ty, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[tx][ty] = True

    heap = []
    while queue:
        x, y, count = queue.popleft()
        if customer[x][y] != -1:
            heapq.heappush(heap, (count, x, y, customer[x][y]))
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] or mat[nx][ny] == 1:
                continue

            queue.append((nx, ny, count + 1))
            visited[nx][ny] = True

    if heap:
        return heapq.heappop(heap)
    return -1, -1, -1, -1

def go_to_dest(num, cx, cy):
    # num번 고객이 cx, cy에 있음 ->? 해당 고객의 도착지까지 구하기
    queue = deque([(cx, cy, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[cx][cy] = True

    while queue:
        x, y, count = queue.popleft()
        if (x, y) == dest[num]:
            return x, y, count
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] or mat[nx][ny] == 1:
                continue

            queue.append((nx, ny, count + 1))
            visited[nx][ny] = True
    return -1, -1, -1


N, M, fuel = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]
tx, ty = map(int, input().split(' '))
tx, ty = tx - 1, ty - 1

customer = [[-1] * N for _ in range(N)]
dest = {}
for i in range(1, M+1):
    sx, sy, ex, ey = map(int, input().split(' '))
    customer[sx-1][sy-1] = i
    dest[i] = (ex-1, ey-1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

is_valid = True
for _ in range(M):
    # 가장 가까운 손님 찾기
    count, cx, cy, num = find_nearest_customer(tx, ty)
    if num == -1 or count > fuel:
        is_valid = False
        break

    customer[cx][cy] = -1
    fuel -= count

    # 택시는 해당 위치로 이동 -> 그 위치에서 해당 손님의 도착지깢지 이동
    tx, ty, count = go_to_dest(num, cx, cy)
    if tx == -1 or count > fuel:
        is_valid = False
        break
    fuel += count


print(-1) if not is_valid else print(fuel)