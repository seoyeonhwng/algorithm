import re

N = int(input())
answer = set()

for _ in range(N):
    cmd = input().split('@')
    if len(cmd) != 2:
        continue
    user_name, domain = cmd

    if not re.fullmatch(r'^\w[a-zA-Z0-9_.]*\w$', user_name):
        continue
    if re.search(r'\.{2,}', user_name):
        continue
    
    user_name = user_name.replace('.', '').lower()
    if len(user_name) < 6 or len(user_name) > 30:
        continue
    
    if not re.fullmatch(r'^([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+$', domain):
        continue

    domain = domain.lower()
    if len(domain) < 3 or len(domain) > 30:
        continue
    
    answer.add(f'{user_name}@{domain}')

print(len(answer))
