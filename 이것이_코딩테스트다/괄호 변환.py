def divide(p):
    left, right, N = 0, 0, len(p)
    
    for i in range(N):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i+1], p[i+1:]

def is_correct(p):
    # 올바른 문자열인지 체크
    stack = []
    for c in p:
        if c == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
    return True if not stack else False

def convert(p):
    new = ''
    for c in p:
        new += ')' if c == '(' else '('
    return new

def solution(p):
    if p == '':
        return ''
    
    u, v = divide(p)
    
    if is_correct(u):
        return u + solution(v)

    return '(' + solution(v) + ')' + convert(u[1:-1])

p = '))((()'
print(solution(p))