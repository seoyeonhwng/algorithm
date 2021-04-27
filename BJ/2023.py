def is_prime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def dfs(num):
    global result
    if len(num) == N:
        result.append(num)
        return

    for w in range(1, 10):
        new_num = num + str(w)
        if is_prime(int(new_num)):
            dfs(new_num)

N = int(input())
result = []
dfs('')

result.sort()
for r in result:
    print(r)