from collections import deque

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def bfs():
    queue = deque([(str(A), 0)])
    visited = set([str(A)])

    while queue:
        num, count = queue.popleft()
        if num == str(B):
            return count

        for i in range(4):
            for j in range(10):
                new = num[:i] + str(j) + num[i+1:]
                if int(new) < 1000 or new in visited or not is_prime(int(new)):
                    continue

                queue.append((new, count + 1))
                visited.add(new)
    return -1

for _ in range(int(input())):
    A, B = map(int, input().split(' '))
    ans = bfs()
    print('Impossible') if ans == -1 else print(ans)