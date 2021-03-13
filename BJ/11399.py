N = int(input())
nums = list(map(int, input().split(' ')))

info = {}
for i, v in enumerate(nums):
    info[i] = v
info = sorted(info.items(), key=lambda x:x[1])

# 걸리는 시간 = 기다리는 시간 + 자기꺼 처리하는 시간 -> 기다리는 시간을 최소로 하자
ans, w_time = 0, 0
for _, t in info:
    ans += (w_time + t)
    w_time += t
print(ans)


