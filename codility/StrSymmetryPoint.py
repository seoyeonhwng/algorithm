# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    if not S or len(S) % 2 == 0:
        return -1
    if len(S) == 1:
        return 0
        
    mid = len(S) // 2
    if S[:mid] == S[mid+1:][::-1]:
        return mid
    return -1
  
    