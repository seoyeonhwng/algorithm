import sys

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2 # mid번 승리
        ratio = int((Y + mid) * 100 / (X + mid))

        if ratio > Z:
            end = mid - 1
        else:
            start = mid + 1
    return end + 1


X, Y = map(int, input().split(' '))
Z = int(Y * 100 / X)
if Z >= 99:
    print(-1)
    sys.exit()

print(binary_search(1, X))