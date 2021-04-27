def get_score(h, d, t):
    # h에 서있는 말을 d로 이동시킬때
    if h == 0:
        candi = [(2, 0), (4, 0), (6, 0), (8, 0), (10, 0)]
    elif h == 2:
        candi = [(4, 0), (6, 0), (8, 0), (10, 0), (12, 0)]
    elif h == 4:
        candi = [(6, 0), (8, 0), (10, 0), (12, 0), (14, 0)]
    elif h == 6:
        candi = [(8, 0), (10, 0), (12, 0), (14, 0), (16, 0)]
    elif h == 8:
        candi = [(10, 0), (12, 0), (14, 0), (16, 0), (18, 0)]
    elif h == 10:
        candi = [(13, 0), (16, 1), (19, 0), (25, 0), (30, 1)]
    elif h == 12:
        candi = [(14, 0), (16, 0), (18, 0), (20, 0), (22, 0)]
    elif h == 14:
        candi = [(16, 0), (18, 0), (20, 0), (22, 0), (24, 0)]
    elif h == 16 and t == 0:
        candi = [(18, 0), (20, 0), (22, 0), (24, 0), (26, 0)]
    elif h == 18:
        candi = [(20, 0), (22, 0), (24, 0), (26, 0), (28, 0)]
    elif h == 20:
        candi = [(22, 0), (24, 0), (25, 0), (30, 0), (35, 0)]
    elif h == 22 and t == 0:
        candi = [(24, 0), (26, 0), (28, 0), (30, 0), (32, 0)]
    elif h == 24 and t == 0:
        candi = [(26, 0), (28, 0), (30, 0), (32, 0), (34, 0)]
    elif h == 26 and t == 0:
        candi = [(28, 0), (30, 0), (32, 0), (34, 0), (36, 0)]
    elif h == 28 and t == 0:
        candi = [(30, 0), (32, 0), (34, 0), (36, 0), (38, 0)]
    elif h == 30 and t == 0:
        candi = [(28, 1), (27, 0), (26, 1), (25, 0), (30, 1)]
    elif h == 32:
        candi = [(34, 0), (36, 0), (38, 0), (40, 0), (-1, 0)]
    elif h == 34:
        candi = [(36, 0), (38, 0), (40, 0), (-1, 0), (-1, 0)]
    elif h == 36:
        candi = [(38, 0), (40, 0), (-1, 0), (-1, 0), (-1, 0)]
    elif h == 38:
        candi = [(40, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0)]
    elif h == 40:
        candi = [(-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0)]
    elif h == 13:
        candi = [(16, 1), (19, 0), (25, 0), (30, 1), (35, 1)]
    elif h == 16 and t == 1:
        candi = [(19, 0), (25, 0), (30, 1), (35, 0), (40, 0)]
    elif h == 19:
        candi = [(25, 0), (30, 1), (35, 0), (40, 0), (-1, 0)]
    elif h == 25:
        candi = [(30, 1), (35, 0), (40, 0), (-1, 0), (-1, 0)]
    elif h == 22 and t == 1:
        candi = [(24, 1), (25, 0), (30, 1), (35, 0), (40, 0)]
    elif h == 24 and t == 1:
        candi = [(25, 0), (30, 1), (35, 0), (40, 0), (-1, 0)]
    elif h == 28 and t == 1:
        candi = [(27, 0), (26, 1), (25, 0), (30, 1), (35, 0)]
    elif h == 27:
        candi = [(26, 1), (25, 0), (30, 1), (35, 0), (40, 0)]
    elif h == 26 and t == 1:
        candi = [(25, 0), (30, 1), (35, 0), (40, 0), (-1, 0)]
    elif h == 25:
        candi = [(30, 1), (35, 0), (40, 0), (-1, 0), (-1, 0)]
    elif h == 30 and t == 1:
        candi = [(35, 0), (40, 0), (-1, 0), (-1, 0), (-1, 0)]
    elif h == 35:
        candi = [(40, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0)]

    return candi[d-1]


def dfs(elements, horses, total, t):
    global answer
    print('++ ', elements, horses, total, t)
    if len(elements) == 0:
        answer = max(answer, total)
        return

     # 4개의 말에 대해 모두 이동
    for i, h in enumerate(horses):
        if h == -1: # 이미 도착해있는 말이라면 pass
            dfs(elements[1:], horses, total, t)
        else:
            score, nt = get_score(h, elements[0], t)
            if score in horses and score != -1:
                dfs(elements[1:], horses, total, t)
            else:
                horses[i] = score
                dfs(elements[1:], horses, total + score, nt)
                horses[i] = h



nums = list(map(int, input().split(' ')))
horses = [0, 0, 0, 0]
answer = 0
dfs(nums, horses, 0, 0)
print(answer)