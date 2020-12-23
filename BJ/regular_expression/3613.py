import re

"""
* 단어는 문자 1개 이상을 의미

* C++
[a-z]+ : 첫번째 단어는 소문자 사용
(_[a-z]+)* : _[a-z]+이 0번 이상 반복
_[a-z]+ : 두번째 단어부터는 앞에 _이 오고 소문자로 구성된 단어가 온다.

* Java
[a-z]+ : 첫번째 단어는 소문자 사용
([A-Z][a-z]*)* : [A-z][a-z]*이 0번 이상 반복
[A-z][a-z]* : 두번째 단어부터는 첫 문자만 대문자로 쓰고 나머지 문자는 소문자가 온다.
"""

c_exp = '[a-z]+(_[a-z]+)*'
j_exp = '[a-z]+([A-Z][a-z]*)*'

var_name = input()
if re.fullmatch(c_exp, var_name):
    converted = ''
    for s in re.split('(_[a-z])', var_name): # () <- keep the separators
        if s.startswith('_'):
            converted += s[-1].upper()
        else:
            converted += s
    print(converted)

elif re.fullmatch(j_exp, var_name):
    converted = ''
    for s in re.split('([A-Z])', var_name): # () <- keep the separators
        if s.isupper():
            converted += f'_{s.lower()}'
        else:
            converted += s
    print(converted)
else:
    print('Error!')