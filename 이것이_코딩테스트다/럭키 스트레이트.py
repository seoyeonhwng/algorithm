N = input()
half = len(N) // 2

left, right = 0, 0
for i in range(half):
    left += int(N[i])

for i in range(half, half * 2):
    right += int(N[i])

print('LUCKY') if left == right else print('READY')