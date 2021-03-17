from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)

    tw = truck_weights.popleft()
    truck, w = deque([[tw, 1]]), tw
    ans = 1

    while truck:
        # 내릴 애가 있다면 내려
        while truck and truck[0][1] == bridge_length:
            tw = truck.popleft()[0]
            w -= tw

        # 태울 수 있다면 태워
        if truck_weights and w + truck_weights[0] <= weight:
            tw = truck_weights.popleft()
            truck.append([tw, 0])
            w += tw
        
        # 하나씩 이동시킴
        N = len(truck)
        for i in range(N):
            truck[i][1] += 1

        ans += 1
    return ans


bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))