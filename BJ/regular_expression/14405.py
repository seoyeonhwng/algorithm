import re

# pi가 0번 이상 반복 가능
# ka가 0번 이상 반복 가능
# chu가 0번 이상 반복 가능
# 위의 조합이 1번 이상 반복 가능
exp = '((pi)*(ka)*(chu)*)+'
result = re.fullmatch(exp, input())

print('YES') if result else print('NO')

"""
# 정규식 사용 안한 버젼

s = input()
while s:
    if s.startswith('pi'):
        s = s[2:]
    elif s.startswith('ka'):
        s = s[2:]
    elif s.startswith('chu'):
        s = s[3:]
    else:
        break

print('YES') if len(s) == 0 else print('NO')
"""