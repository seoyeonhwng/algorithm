# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6

    # 배수는 짝으로 존재하니까 +2씩!
    # 이렇게 계산하면 O(sqrt(N))
    i = 1
    count = 0
    
    while i * i < N:
        if N % i == 0:
            count += 2
        i += 1
        
    if i * i == N:
        count += 1
    return count
