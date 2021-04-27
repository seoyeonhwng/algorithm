for _ in range(int(input())):
    N = int(input())
    prices = list(map(int, input().split(' ')))

    # price의 최댓값보다 작으면 사고 최댓값일땐 판다!
    # 최댓값보다 크면 팔고 그 뒤의 값들 중에 최댓값으로 갱신
    # 최댓값을 매번 갱신하는 일이 오래 걸림 -> 뒤부터 살펴본다!!
    max_price, answer = 0, 0

    for i in range(N-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            answer += (max_price - prices[i])
    print(answer)