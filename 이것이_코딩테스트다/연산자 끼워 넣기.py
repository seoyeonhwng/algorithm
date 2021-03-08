import sys


def dfs(i, n, op):
    global min_val, max_val

    if i == N-1:
        min_val = min(n, min_val)
        max_val = max(n, max_val)
        return

    for j, o in enumerate(op):
        if o == 0:
            continue
        
        w = nums[i+1]
        new_op = op[:j] + [o - 1] + op[j+1:]
        if j == 0:
            dfs(i+1, n + w, new_op)
        elif j == 1:
            dfs(i+1, n - w, new_op)
        elif j == 2:
            dfs(i+1, n * w, new_op)
        else:
            new_num = -(abs(n) // w) if n < 0 else n // w
            dfs(i+1, new_num, new_op)

    


N = int(input())
nums = list(map(int, input().split(' ')))
op = list(map(int, input().split(' ')))

min_val, max_val = sys.maxsize, -sys.maxsize
dfs(0, nums[0], op)
print(max_val)
print(min_val)
