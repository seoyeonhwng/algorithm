import re

N = int(input())
strings = [input() for _ in range(N)]

nums = []
for s in strings:
    tmp = re.split('[a-z]', s) # 소문자 기준으로 split
    nums += [int(t) for t in tmp if t]

for n in sorted(nums):
    print(n)