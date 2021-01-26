def check(path):
    c1, c2 = 0, 0
    for p in path:
        if p in ['a', 'e', 'i', 'o', 'u']:
            c1 += 1
        else:
            c2 += 1
    return c1 >= 1 and c2 >= 2

def dfs(path):
    if len(path) == L:
        # 모음 자음 검사
        if check(path):
            result.append(path)
        return
    
    for c in chars:
        if path == '':
            dfs(path + c)
        elif path[-1] < c:
            dfs(path + c)

L, C = map(int, input().split(' '))
chars = sorted(input().split(' '))

result = []
dfs('')
for r in sorted(result):
    print(r)