import sys

for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split(' ')))

    # n개의 배열이 있을때 인접하는 원소의 최대 높이차는 1번과 3번, 2번과 4번, ... n-2번과 n번 중 최대
    nums.sort()
    answer = -sys.maxsize

    for i in range(N-2):
        answer = max(answer, abs(nums[i] - nums[i+2]))
    print(answer)
