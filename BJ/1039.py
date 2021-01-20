from collections import deque
from itertools import combinations
from copy import deepcopy

def get_possible(num):
    possible = set()
    lst = [i for i in range(len(str(num)))]

    for a, b in list(combinations(lst, 2)):
        nn = list(str(deepcopy(num)))
        nn[a], nn[b] = nn[b], nn[a]

        if nn[0] == '0':
            continue
        possible.add(int(''.join([n for n in nn])))
    return possible

def bfs():
    queue = deque([N])
    count = K
    
    while queue:
        if count == 0:
            return max(queue)

        possible = set()
        for _ in range(len(queue)):
            num = queue.popleft()
            possible.update(get_possible(num))
        queue.extend(list(possible))
        count -= 1
        
    return -1



N, K = map(int, input().split(' '))
print(bfs())