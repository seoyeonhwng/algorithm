import re

while True:
    try:
        string = input()
    except:
        break

    l_count = len(re.findall('[a-z]', string)) # 소문자
    u_count = len(re.findall('[A-Z]', string)) # 대문자
    n_count = len(re.findall('[0-9]', string)) # 숫자
    s_count = len(re.findall('\s', string)) # 공백
    print(f'{l_count} {u_count} {n_count} {s_count}')