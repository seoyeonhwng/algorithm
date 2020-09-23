# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import collections

def solution(A):
    # write your code in Python 3.6
    if not A:
        return -1
        
    counter = collections.Counter(A)
    for k, count in counter.items():
        if count > (len(A) // 2):
            return A.index(k)
            
    return -1