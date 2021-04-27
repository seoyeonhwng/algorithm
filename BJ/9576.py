import sys
input = sys.stdin.readline


def find_idx(a, b):
    for i in range(a, b+1):
        if not books[i]:
            return i
    return 0

for _ in range(int(input())):
    N, M = map(int, input().split(' '))
    data = []
    for _ in range(M):
        a, b = map(int, input().split(' '))
        data.append((a, b))

    # b, a가 작은 순서대로 정렬 -> a부터 b까지 중에서 가장 작은 번호로 반환 -> 그리디
    # b는 자신이 받을 수 있는 가장 큰 번호이므로 이 번호가 작은 순으로 책을 배정함
    data = sorted(data, key=lambda x:(x[1], x[0]))
    books = [False] * (N+1)
    for a, b in data:
        idx = find_idx(a, b)
        if idx > 0:
            books[idx] = True
    print(sum(books))
