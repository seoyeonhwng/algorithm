N = int(input())
A = list(map(int, input().split(' ')))
M = int(input())
nums = list(map(int, input().split(' ')))

A = set(A)
for n in nums:
    if n in A:
        print(1)
    else:
        print(0)