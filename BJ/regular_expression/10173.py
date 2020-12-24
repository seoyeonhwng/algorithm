import re

while True:
    s = input()
    if s == 'EOI':
        break
    
    if re.search('nemo', s.lower()):
        print('Found')
    else:
        print('Missing')