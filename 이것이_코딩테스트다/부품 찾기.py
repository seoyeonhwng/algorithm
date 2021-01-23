import sys
from bisect import bisect_left, bisect_right

N = int(input())
products = list(map(int, sys.stdin.readline().rstrip().split(' ')))
M = int(input())
want = list(map(int, sys.stdin.readline().rstrip().split(' ')))

# 이진탐색으로 w가 product안에 있는지 확인해보자
products.sort()
for w in want:
    if bisect_right(products, w) != bisect_left(products, w): # w가 존재함
        print('yes')
    else:
        print('no')
