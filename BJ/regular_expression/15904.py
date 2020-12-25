import re

string = input()
string = re.sub('[^A-Z]', '', string)

if re.fullmatch('[A-Z]*U[A-Z]*C[A-Z]*P[A-Z]*C[A-Z]*', string):
    print('I love UCPC')
else:
    print('I hate UCPC')