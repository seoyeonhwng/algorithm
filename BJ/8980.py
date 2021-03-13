from collections import defaultdict, deque
import heapq

N, C = map(int, input().split(' '))
boxes = []
M = int(input())
for _ in range(M):
    u, v, w = map(int, input().split(' '))
    boxes.append((u, v, w))

boxes = sorted(boxes, key=lambda x:(x[1], x[0], x[2]))
truck = [0] * (N+1)
ans = 0
for i in range(M):
    s, e, w = boxes[i]

    # 배송 구간에 있는 역의 최대 택배 개수를 구함 (limit)
    weight = 0
    for j in range(s, e):
        weight = max(weight, truck[j])
    
    # 최대 C - weight만큼 실을 수 있음 -> w와 비교해서 작은 값을 실자
    weight = min(C - weight, w)
    ans += weight

    for j in range(s, e):
        truck[j] += weight
print(ans)
