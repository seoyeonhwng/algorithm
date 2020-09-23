# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    count = 0
    stack = []
    
    # 벽의 높이가 낮아지는 순간이 문제!
    for h in H:
        while stack and stack[-1] > h: 
            # 피크가 지나고 자신보다 큰 벽은 블럭으로 처리
            stack.pop()
        
        if not stack or stack[-1] < h:
            stack.append(h)
            count += 1
            
    return count
