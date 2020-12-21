cmd = input()
if len(cmd.split(' ')) == 2:
    N, M = cmd.split(' ')
else:
    N = cmd
    M = input()

height = [[0] * int(N) for _ in range(int(N))]
for _ in range(int(M)):
    a, b = map(int, input().split(' '))
    height[a-1][b-1] = 1

# 플로이드 와샬 -> 연결되어 있는 노드들 1로 표시
for k in range(int(N)):
    for i in range(int(N)):
        for j in range(int(N)):
            if height[i][j] == 1 or (height[i][k] == 1 and height[k][j] == 1):
                height[i][j] = 1

count = 0
for i in range(int(N)):
    known_height = 0
    for j in range(int(N)):
        known_height += height[i][j] + height[j][i] # 나보다 작은 놈 + 나보다 큰 놈
    
    if known_height == int(N) - 1:
        count += 1

print(count)

"""
그래프에서 가능한 모든 노드 쌍에 대한 최단 거리를 구해야하므로 플로이드 와샬로 해결한다!
"""
