import heapq

K, N = map(int, input().split(' '))
primes = list(map(int, input().split(' ')))

heap = []
for p in primes:
    heapq.heappush(heap, p)

count = 0
while heap and count < N:
    top = heap[0]
    while heap and top == heap[0]: # 중복된 원소들은 한번에 제거
        n = heapq.heappop(heap)

    for p in primes:
        heapq.heappush(heap, n * p)
    count += 1
print(n)