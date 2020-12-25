import re

N = int(input())
exp = r'(http|ftp|gopher)://([\w\.\-]+)(:[0-9]+)?(/[\S]+)*'

for i in range(N):
    s = input()
    units = re.findall(exp, s)[0]
    print(f'URL #{i+1}')
    print(f'Protocol = {units[0]}')
    print(f'Host     = {units[1]}')

    port = '<default>' if not units[2] else units[2][1:]
    print(f'Port     = {port}')

    path = '<default>' if not units[3] else units[3][1:]
    print(f'Path     = {path}\n')