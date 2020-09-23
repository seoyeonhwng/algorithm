# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import sys

def solution(A):
    # write your code in Python 3.6
    profit = 0
    min_price = sys.maxsize
    
    # 최솟값과 최댓값을 계속 갱신
    for price in A:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
        
    return profit