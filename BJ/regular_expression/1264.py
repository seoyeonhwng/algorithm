import re

while True:
    s = input()
    if s == '#':
        break

    print(len(re.findall('(?i)[aeiou]', s))) # (?i)는 대소문자 무시