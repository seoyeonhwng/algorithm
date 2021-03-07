from bisect import bisect_left, bisect_right

def get_count(stages, num):
    return bisect_right(stages, num) - bisect_left(stages, num)

def solution(N, stages):
    stages.sort()
    answer = {}
    total = len(stages)
    
    for i in range(1, N+1):
        count = get_count(stages, i)
        if count == 0:
            answer[i] = 0
        else:
            answer[i] = count / total
            total -= count
    
    tmp = sorted(answer.items(), key=lambda x:x[1], reverse=True)
    return [t[0] for t in tmp]