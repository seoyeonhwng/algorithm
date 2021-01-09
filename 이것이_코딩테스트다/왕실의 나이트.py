pos = input()
x, y = int(pos[1])-1, ord(pos[0])-ord('a')

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
ans = 0

for i in range(8):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        ans += 1
print(ans)