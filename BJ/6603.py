def dfs(i, path):
    if i == 6:
        result.append(path)
        return
    
    for w in nums[i:]:
        if (not path) or (path and w > path[-1]):
            dfs(i+1, path + [w])

while True:
    nums = list(map(int, input().split(' ')))
    N = nums.pop(0)
    if N == 0:
        break

    result = []
    dfs(0, [])
    result.sort()
    for r in result:
        print(*r)
    print()

