import re

s = input()

words = re.split(' |-', s)
count = len(words)

for w in words:
    exp = "(c|j|n|m|t|s|l|d|qu)'[aeiouh]"
    if re.match(exp, w):
        count += 1
   
print(count)
