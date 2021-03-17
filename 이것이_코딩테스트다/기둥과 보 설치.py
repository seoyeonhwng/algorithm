def zero_possible(i, j, answer):
    # x, y 좌표에 기둥 세우는 조건을 하나라도 만족하는지
    if j == 0:
        return True
    if [i-1, j, 1] in answer or [i, j, 1] in answer:
        return True
    if [i, j-1, 0] in answer:
        return True
    return False

def one_possible(i, j, answer):
    # x, y좌표에 보 세우는 조건을 하나라도 만족하는지
    if [i, j-1, 0] in answer or [i+1, j-1, 0] in answer:
        return True
    if [i-1, j, 1] in answer and [i+1, j, 1] in answer:
        return True
    return False

def possible(answer):
    for x, y, t in answer:
        poss = zero_possible(x, y, answer) if t == 0 else one_possible(x, y, answer)
        if not poss:
            return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0: # 삭제하는 경우
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
        
        if b == 1: # 추가하는 경우
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])

    answer.sort()
    return answer
        

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
solution(n, build_frame)