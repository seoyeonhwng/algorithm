import heapq

N = int(input())
K = int(input())
students = list(map(int, input().split(' ')))

photos = {}
for i, s in enumerate(students):
    if s in photos: # 현재 게시된 학생은 추천받은 횟수만 증가
        value, idx = photos[s]
        photos[s] = (value + 1, idx)
    else: # 현재 게시 안됨
        if len(photos) < N: # 빈 공간이 있으니까 그냥 게시하면 됨
            photos[s] = (1, i)
        else: # 추천 횟수가 가장 작고 그 중에서 i가 가장 작은 놈 선택
            min_s = sorted(photos.items(), key=lambda x : (x[1][0], x[1][1]))[0][0]
            del photos[min_s]
            photos[s] = (1, i)

print(*sorted(photos.keys()))