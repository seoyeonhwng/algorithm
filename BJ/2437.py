N = int(input())
nums = list(map(int, input().split(' ')))

nums.sort()
target = 1
for n in nums:
    if target < n:
        break
    target += n
print(target)

"""
* 리스트의 조합으로 만들 수 없는 최소값 찾는 문제
- target : target 전까지 다 만들 수 있음
- 리스트를 정렬한 뒤 작은 수부터 하나씩 더해감
- 이때 더하려는 수가 target보다 크다면 target을 만들 수 없음!!
"""