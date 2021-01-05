from collections import deque

def calculate(n, method):
    if method == 'D':
        return (2 * n) % 10000
    if method == 'S':
        return (n -1 ) % 10000
    if method == 'L':
        return (n % 1000) * 10 + n // 1000 # 문자열 인덱싱보다 수식으로 처리하는 것이 더 빠름!!!!
    if method == 'R':
        return (n % 10) * 1000 + n // 10

def bfs(start):
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        v, path = queue.popleft()
        if v == B:
            print(*path, sep='')
            return

        dn = calculate(v, 'D')
        if dn not in visited:
            queue.append((dn, path + ['D']))
            visited.add(dn)

        ds = calculate(v, 'S')
        if ds not in visited:
            queue.append((ds, path + ['S']))
            visited.add(ds)

        dl = calculate(v, 'L')
        if dl not in visited:
            queue.append((dl, path + ['L']))
            visited.add(dl)

        dr = calculate(v, 'R')
        if dr not in visited:
            queue.append((dr, path + ['R']))
            visited.add(dr)


T = int(input())
for _ in range(T):
    A, B = map(int, input().split(' '))

    # A와 B까지의 bfs!
    bfs(A)