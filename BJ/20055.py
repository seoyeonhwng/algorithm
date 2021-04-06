N, K = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

answer = 1
robots = [False] * N

while True:
    # 컨베이어 벨터 한 칸 이동
    nums = [nums[-1]] + nums[:-1]
    robots = [robots[-1]] + robots[:-1]
    robots[-1] = False

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다
    for i in range(N-2, -1, -1):
        if robots[i] and not robots[i+1] and nums[i+1] >= 1:
            robots[i], robots[i+1] = False, True
            nums[i+1] -= 1
    robots[-1] = False
    
    # 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if not robots[0] and nums[0] >= 1:
        robots[0] = True
        nums[0] -= 1
 
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
    count = 0
    for i in range(2*N):
        if nums[i] <= 0:
            count += 1

    if count >= K:
        break
    answer += 1

print(answer)

