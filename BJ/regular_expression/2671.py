import re

# +는 한번 이상 반복
# (A|B)는 A 또는 B 중에 하나만 선택
exp = '(100+1+|01)+'
result = re.fullmatch(exp, input())

print('SUBMARINE') if result else print('NOISE')