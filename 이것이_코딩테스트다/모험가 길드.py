from collections import Counter

N = int(input())
nums = list(map(int, input().split(' ')))
counter = Counter(nums)
counter = sorted(counter.items(), key=lambda x:x[0])

ans, res = 0, 0
for key, cnt in counter:
    q, r = divmod(cnt, key)
    ans += q
    res += r
    
    q, r = divmod(res, key)
    ans += q
    res = r
print(ans)

"""
* 풀이
- 오름차순으로 정렬 후 현재 그룹을 하나씩 만들고 총 그룹을 계산
- 그룹의 수를 최대한 만들기 위해 공포도가 낮은 모험가부터 그룹을 생성 = greedy

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도가 오름차순으로 정렬된 상태
    count += 1 # 현재 그룹에 포함
    if count >= i: # 그룹 결성
        result += 1
        count = 0
"""