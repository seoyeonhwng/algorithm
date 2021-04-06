import heapq

N, M = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))
heapq.heapify(cards)

# 최소한의 점수를 만들기 위해 각 단계마다 가장 작은 카드 두개를 더함!
for _ in range(M):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    heapq.heappush(cards, x + y)
    heapq.heappush(cards, x + y)
print(sum(cards))