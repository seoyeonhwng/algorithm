exp = input()
# 값을 최소로 만들기 위해서는 -를 기준으로 괄호!

exp = exp.split('-')
nums = []
for e in exp:
    num = 0
    for n in e.split('+'):
        num += int(n)
    nums.append(num)

N = len(nums)
ans = nums[0]
for i in range(1, N):
    ans -= nums[i]
print(ans)
