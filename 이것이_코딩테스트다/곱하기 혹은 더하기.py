S = list(map(int, list(input())))
n = len(S)

if n == 1:
    print(S[0])
else:
    val = max(S[0] * S[1], S[0] + S[1])
    for i in range(2, n):
        val = max(val * S[i], val + S[i])
    print(val)

    