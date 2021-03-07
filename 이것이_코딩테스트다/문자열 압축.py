from collections import deque
import sys

def get_split_word(unit, N, S):
    i = 0
    words = []
    while i < N:
        char = ''.join(S[i:i+unit])
        words.append(char)
        i += unit
    return words

def solution(s):
    N = len(s)
    if N == 1:
        return 1
    
    answer = 1000
    for unit in range(1, N//2+1):
        words = get_split_word(unit, N, s)
        queue = deque(words)
        new_str = ''

        while queue:
            a, count = queue.popleft(), 1
            while queue and queue[0] == a:
                queue.popleft()
                count += 1
            
            new_str = new_str + f'{count}{a}' if count > 1 else new_str + a
        answer = min(answer, len(new_str))

    return answer