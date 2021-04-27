from itertools import combinations
from copy import deepcopy
from collections import deque, defaultdict
import heapq


def get_enemy(enemy, cx, cy):
    heap = []
    for x, y in enemy:
        d = abs(cx - x) + abs(cy - y)
        if d <= D:
            heapq.heappush(heap, (d, y, x))
    
    return heap


def play(enemy, combi):
    # enemy는 적의 위치가 저장 / combi는 궁수의 위치가 저장
    result = 0
    while True:
        if not enemy:
            return result

        # 각 궁수마다 조건에 맞는 적을 선택
        target = set()
        for cx, cy in combi:
            candi = get_enemy(enemy, cx, cy)
            if not candi:
                continue
            target.add((candi[0][2], candi[0][1]))

        for x, y in target:
            enemy.remove((x, y))
            result += 1

        enemy = [(x+1, y) for x, y in enemy if x + 1 < N]
    return result


N, M, D = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]
enemy = []
for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            enemy.append((i, j))

candi = [(N, i) for i in range(M)]
answer = 0
for combi in list(combinations(candi, 3)):
    new_enemy = deepcopy(enemy)
    result = play(new_enemy, combi)
    answer = max(answer, result)
print(answer)