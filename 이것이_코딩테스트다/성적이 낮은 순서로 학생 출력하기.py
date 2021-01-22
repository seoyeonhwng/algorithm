info = {}
for _ in range(int(input())):
    name, score = input().split(' ')
    info[name] = score

# 성적이 낮은 순서대로 정렬
info = sorted(info.items(), key=lambda x: x[1])
print(*[i[0] for i in info])