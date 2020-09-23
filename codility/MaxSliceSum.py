# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys

def solution(A):
    # write your code in Python 3.6
    current_sum = 0
    max_sum = -sys.maxsize
    
    # 최댓값 게속 갱신 
    # 계속 더하다가 current_sum이 음수가 되면 버린다!
    for a in A:
        current_sum = max(a, current_sum + a)
        max_sum = max(max_sum, current_sum)
    
    return max_sum