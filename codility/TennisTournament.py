# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(P, C):
    # write your code in Python 3.6
    pair = P // 2
    return min(pair, C)