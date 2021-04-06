import heapq

N = int(input())
classes = []
for _ in range(N):
    s, e = map(int, input().split(' '))
    classes.append([s, e])

# 최소한의 강의실 사용을 위해 강의 시작 순서대로 정렬
classes = sorted(classes, key=lambda x:x[0])
current = []

for s, e in classes:
    if len(current) != 0 and s >= current[0]: # 가장 먼저 끝나는 강의와 비교
        heapq.heappop(current)
    heapq.heappush(current, e)
print(len(current))