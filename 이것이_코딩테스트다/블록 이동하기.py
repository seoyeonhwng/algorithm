from collections import deque


def bfs(board):
    N = len(board)
    visited = []
    queue = deque([(0, 0, 0, 1, 0)])
    visited.append({(0, 0), (0, 1)})

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        ax, ay, bx, by, count = queue.popleft()
        if (ax, ay) == (N-1, N-1) or (bx, by) == (N-1, N-1):
            return count

        # 한칸씩 이동
        for i in range(4):
            nax, nay = ax + dx[i], ay + dy[i]
            if nax < 0 or nax >= N or nay < 0 or nay >= N or board[nax][nay] == 1:
                continue
            nbx, nby = bx + dx[i], by + dy[i]
            if nbx < 0 or nbx >= N or nby < 0 or nby >= N or board[nbx][nby] == 1:
                continue
            if {(nax, nay), (nbx, nby)} in visited:
                continue
            queue.append((nax, nay, nbx, nby, count + 1))
            visited.append({(nax, nay), (nbx, nby)})
        
        # 회전하는 경우
        # 가로로 놓여있는 경우
        if ax == bx:
            for i in [1, -1]:
                if ax + i < 0 or ax + i >= N or bx + i < 0 or bx + i >= N:
                    continue
                if board[ax+i][ay] == 1 or board[bx+i][by] == 1:
                    continue
                if {(ax, ay), (ax + i, ay)} not in visited:
                    queue.append((ax, ay, ax + i, ay, count + 1))
                    visited.append({(ax, ay), (ax + i, ay)})
                if {(bx, by), (bx + i, by)} not in visited:
                    queue.append((bx, by, bx + i, by, count + 1))
                    visited.append({(bx, by), (bx + i, by)})
        
        # 세로로 놓여있는 경우
        if ay == by:
            for i in [1, -1]:
                if ay + i < 0 or ay + i >= N or by + i < 0 or by + i >= N:
                    continue
                if board[ax][ay+i] == 1 or board[bx][by+i] == 1:
                    continue
                if {(ax, ay), (ax, ay + i)} not in visited:
                    queue.append((ax, ay, ax, ay + i, count + 1))
                    visited.append({(ax, ay), (ax, ay + i)})
                if {(bx, by), (bx, by + i)} not in visited:
                    queue.append((bx, by, bx, by + i, count + 1))
                    visited.append({(bx, by), (bx, by + i)})
                


def solution(board):
    # (1, 1)에서 부터 (N, N)까지 최단 거리
    answer = bfs(board)
    return answer
  
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))