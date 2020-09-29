# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections, itertools

def solution(A, X):
    # write your code in Python 3.6
    # binary search를 하는 것이 핵심!
    if not A:
        return 0
    counter = collections.Counter(A)
    candidates = []
    answer = 0
    
    for k, v in counter.items():
        if v >= 2:
            candidates.append(k)
        if v >= 4 and k * k >= X:
            answer += 1
    
    candidates.sort()
    for i in range(len(candidates)):
        begin = i + 1
        end = len(candidates) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if candidates[i] * candidates[mid] >= X:
                end = mid - 1
            else:
                begin = mid + 1
                
        answer += len(candidates) - (end + 1)
        if answer > 1000000000:
            return -1
    
    return answer