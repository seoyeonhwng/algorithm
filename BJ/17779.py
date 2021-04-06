from collections import defaultdict
import sys
input = sys.stdin.readline

def calculate(x, y, d1, d2):
    label = [[-1] * (N+1) for _ in range(N+1)]
    score = defaultdict(int)

    # 경계선
    nx, ny, nx2, ny2 = x, y, x + d2, y + d2
    for _ in range(d1+1):
        label[nx][ny] = 5
        label[nx2][ny2] = 5
        nx, ny = nx + 1, ny - 1
        nx2, ny2 = nx2 + 1, ny2 -1
    
    nx, ny, nx2, ny2 = x, y, x + d1, y - d1
    for _ in range(d2+1):
        label[nx][ny] = 5
        label[nx2][ny2] = 5
        nx, ny = nx + 1, ny + 1
        nx2, ny2 = nx2 + 1, ny2 + 1

    # 경계선 채우기
    for row in label:
        start, end = 1, N
        while start < N + 1 and row[start] != 5:
            start += 1
        while end >= 0 and row[end] != 5:
            end -= 1
        for i in range(start, end):
            row[i] = 5

    # 나머지
    for r in range(1, N+1):
        for c in range(1, N+1):
            if label[r][c] == -1 and (1 <= r < x + d1) and (1 <= c <= y):
                score[1] += mat[r][c]
            elif label[r][c] == -1 and (1 <= r <= x + d2) and (y < c <= N):
                score[2] += mat[r][c]
            elif label[r][c] == -1 and (x + d1 <= r <= N) and (1 <= c < y - d1 + d2):
                score[3] += mat[r][c]
            elif label[r][c] == -1 and (x + d2 < r <= N) and (y - d1 + d2 <= c <= N):
                score[4] += mat[r][c]
            elif label[r][c] == 5:
                score[5] += mat[r][c]

    min_v = min(score.values())
    max_v = max(score.values())
    return max_v, min_v



N = int(input())
mat = [[]]
for _ in range(N):
    tmp = [0] + list(map(int, input().split(' ')))
    mat.append(tmp)

answer = sys.maxsize
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                # 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
                if (1 <= x < x + d1 + d2 <= N) and (1 <= y-d1 < y < y + d2 <= N):
                    max_v, min_v = calculate(x, y, d1, d2)
                    answer = min(answer, max_v - min_v)

print(answer)