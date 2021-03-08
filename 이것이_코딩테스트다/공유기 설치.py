N, C = map(int, input().split(' '))
house = [int(input()) for _ in range(N)]

# 찾고자 하는 값 = 최대 간격 -> 이 간격을 이진 탐색으로 찾는다
# 특정 간격으로 공유기 C개를 설치할 수 있는지 체크
# C개보다 적게 설치할 수 있다면 간격을 줄이고, 많이 설치할 수 있다면 간격을 늘림

house.sort()
start = 1
end = house[-1] - house[0]
ans = start

while start <= end:
    mid = (start + end) // 2

    # mid 간격으로 공유기 몇개를 설치할 수 있는지 체크
    val, count = house[0], 1
    for i in range(1, N):
        if house[i] >= val + mid:
            val = house[i]
            count += 1

    if count >= C: # 공유기 너무 많이 설치 -> 간격 증가
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
