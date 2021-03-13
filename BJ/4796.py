import sys
input = sys.stdin.readline

i = 0
while True:
    i += 1
    L, P, V = map(int, input().split(' '))
    if (L, P, V) == (0, 0, 0):
        break
    # P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를
    q, r = divmod(V, P)
    ans = q * L + min(r, L)
    print(f'Case {i}: {ans}')