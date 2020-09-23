# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import collections

def solution(A):
    # write your code in Python 3.6
    counter_r = collections.Counter(A)
    counter_l = collections.Counter()
    
    count = 0
    count_r = len(A)
    count_l = 0
    
    leader_l = A[0]
    count_leader_l = 0
    
    for i in range(len(A) - 1):
        counter_l[A[i]] += 1
        counter_r[A[i]] -= 1
        count_l += 1
        count_r -= 1
        
        # update left leader 
        # most_common가 O(n)이여서 사용하면 timeout!
        if counter_l[A[i]] > count_leader_l:
            leader_l = A[i]
            count_leader_l = counter_l[A[i]]
        
        # leader인지 체크
        if count_leader_l / count_l > 0.5 and counter_r[leader_l] / count_r > 0.5:
            count += 1
    
    return count