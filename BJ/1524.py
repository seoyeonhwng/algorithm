from collections import deque, defaultdict
from copy import deepcopy


def bfs(mat):
    queue = deque([mat])
    count = defaultdict(int)
    count[mat] = 0

    while queue:
        v = queue.popleft()
        if v == '123456780':
            return count[v]

        # 0의 위치를 찾아서 0의 상하좌우로 이동 가능
        index = v.index('0')
        x, y = index // 3, index % 3

        for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                tmp = list(deepcopy(v))
                tmp[new_index], tmp[index] = tmp[index], tmp[new_index]
                tmp = ''.join([t for t in tmp])

                if tmp not in count: # BFS할때는 중복체크 꼭하자!!!
                    queue.append(tmp)
                    count[tmp] = count[v] + 1
    
    return -1

# 출발점(빈칸의 첫 위치)으로부터 도착점(맨 아래 오른쪽)까지의 최단 거리 -> BFS
# 이차원배열을 문자열로 바꿔서 다루면 메모리 초과 방지할 수 있음!
mat = ''
for _ in range(3):
    mat += input().replace(' ', '')
print(bfs(mat))