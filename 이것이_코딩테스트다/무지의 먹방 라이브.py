import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 음식 먹는데 걸리는 시간이 가장 적은 애부터 없애감
    N, heap = len(food_times), []
    for i, t in enumerate(food_times):
        heapq.heappush(heap, (t, i+1))
    
    total, prev = 0, 0
    while total + (heap[0][0] - prev) * N <= k:
        now = heapq.heappop(heap)[0]
        total += (now - prev) * N
        N -= 1
        prev = now
    
    # 남은 음식 중에서 몇 번째인지 확인
    result = sorted(heap, key=lambda x:x[1])
    return result[(k - total) % N][1]






food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
