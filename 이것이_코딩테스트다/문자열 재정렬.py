S = input()
char, num = [], 0
for s in list(S):
    if 'A' <= s <= 'Z':
        char.append(s)
    else:
        num += int(s)

char.sort()
if num != 0: # 숫자가 있는 경우만 뒤에 삽입!!!! 빼먹지말자
    char.append(str(num))
print(''.join(char))