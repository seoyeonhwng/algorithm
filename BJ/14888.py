import sys

def dfs(idx, ops, total):
    global min_val, max_val
    if idx == N-1:
        min_val = min(min_val, total)
        max_val = max(max_val, total)
        return
    
    for i, o in enumerate(ops):
        if o == 0:
            continue

        new_op = ops[:i] + [o-1] + ops[i+1:]
        if i == 0:
            dfs(idx + 1, new_op, total + nums[idx+1])
        elif i == 1:
            dfs(idx + 1, new_op, total - nums[idx+1])
        elif i == 2:
            dfs(idx + 1, new_op, total * nums[idx+1])
        else:
            tmp = -(abs(total) // nums[idx+1]) if total < 0 else total // nums[idx+1]
            dfs(idx + 1, new_op, tmp)

N = int(input())
nums = list(map(int, input().split(' ')))
op = list(map(int, input().split(' ')))

min_val, max_val = sys.maxsize, -sys.maxsize
dfs(0, op, nums[0])
print(max_val)
print(min_val)