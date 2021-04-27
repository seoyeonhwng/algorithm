def get_idx(i):
    if i == 0 or answer[i] == 0:
        return i
    return get_idx(i-1)

# 점수의 최대값 -> 과제를 많이 (최대한 마감일에 가깝게) + 점수를 높게 (최대한 높은 점수)
N = int(input())
data = []
for _ in range(N):
    d, w = map(int, input().split(' '))
    data.append([w, d])

# 점수를 높은 순으로 정렬
data.sort(reverse=True)

answer = [0] * 1001
for w, d in data:
    idx = get_idx(d)
    if idx == 0:
        continue
    answer[idx] = w # d일때 w를 해! 이런 식으로 지정

print(sum(answer))