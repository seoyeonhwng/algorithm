from copy import deepcopy

def rotate_key(key):
    return list(zip(*key[::-1]))

def fill_lock(lock, lock_N, lock_M, key_N, key_M):
    new_M = lock_M + 2 * (key_M - 1)
    new_lock = [[-1] * new_M for _ in range(key_N-1)]

    for i in range(lock_N):
        tmp = [-1] * (key_M-1) + lock[i] + [-1] * (key_M-1)
        new_lock.append(tmp)
    
    for i in range(key_M-1):
        new_lock.append([-1] * new_M)
    return new_lock

def is_fit(n, m, key, lock, hole):
    key_N, key_M, count = len(key), len(key[0]), 0
    for i in range(key_N):
        for j in range(key_M):
            if lock[n+i][m+j] == -1:
                continue

            if key[i][j] == 1:
                if lock[n+i][m+j] == 1:
                    return False
                count += 1
    
    return hole == count


def solution(key, lock):
    lock_N, lock_M = len(lock), len(lock[0])
    hole = 0
    for i in range(lock_N):
        for j in range(lock_M):
            if lock[i][j] == 0:
                hole += 1

    key_N, key_M = len(key), len(key[0])
    lock = fill_lock(lock, lock_N, lock_M, key_N, key_M)
    lock_N, lock_M = len(lock), len(lock[0])

    for i in range(lock_N-key_N+1):
        for j in range(lock_M-key_M+1):
            for _ in range(4):
                if is_fit(i, j, key, lock, hole):
                    return True
                key = rotate_key(key)
    return False
            
            

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))