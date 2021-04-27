import sys

def dfs(idx, sub_total):
    global answer
    if idx == len(op):
        answer = max(answer, int(sub_total))
        return
    
    dfs(idx + 1, eval(f'{sub_total}{op[idx]}{nums[idx+1]}'))

    if idx + 1 < len(op):
        tmp = eval(f'{nums[idx+1]}{op[idx+1]}{nums[idx+2]}')
        dfs(idx + 2, eval(f'{sub_total}{op[idx]}{tmp}'))
        

N = int(input())
string = input()

op, nums = [], []
for c in string:
    if c.isdigit():
        nums.append(c)
    else:
        op.append(c)
 
answer = -sys.maxsize
dfs(0, nums[0])
print(answer)