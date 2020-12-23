import re

# pi가 0번 이상 반복 가능
# ka가 0번 이상 반복 가능
# chu가 0번 이상 반복 가능
# 위의 조합이 1번 이상 반복 가능
exp = '((pi)*(ka)*(chu)*)+'
result = re.fullmatch(exp, input())

print('YES') if result else print('NO')