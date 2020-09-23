# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys

def solution(A):
    # write your code in Python 3.6
    sum_l = [0] * len(A)
    sum_r = [0] * len(A)
    max_sum = -sys.maxsize
    
    # 왼쪽에서부터 더해가면서 최대합을 구한다
    # A[X + 1] + A[X + 2] + ... + A[Y - 1]
    for i in range(1, len(A)-2):
        sum_l[i] = max(sum_l[i-1] + A[i], 0)
        
    # 오른쪽에서부터 더해가면서 최대합을 구한다
    # A[Y + 1] + A[Y + 2] + ... + A[Z - 1]
    for i in range(len(A)-2, 1, -1):
        sum_r[i] = max(sum_r[i+1] + A[i], 0)
    
    # Y의 값을 기준으로 왼쪽 합 + 오른쪽 합이 최대가 되는 순간을 찾는다!
    # 나는 왜 이런 생각을 못할까.....
    for i in range(1, len(A)-1):
        max_sum = max(max_sum, sum_l[i - 1] + sum_r[i + 1])
        
    return max_sum