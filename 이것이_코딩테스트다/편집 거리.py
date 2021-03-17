from collections import defaultdict
from copy import deepcopy
import sys

def get_idx(candi, B):
    N = min(len(candi), len(B))
    for i in range(N):
        if candi[i] != candi[B]:
            return i
    return -1
    
A = input()
B = input()

len_A, len_B = len(A), len(B)
dp = defaultdict(list)
dp[0].append(A)

ans = sys.maxsize
for i in range(1, len_B+1):
    for candi in dp[i-1]:
        idx = get_idx(candi, B) # 최초로 다른 인덱스 반환
        if idx == -1:
            print(i-1)
            sys.exit()

        dp[i].append(candi[:idx] + B[idx] + candi[idx+1:])
        if len(candi) > len_B:
            dp[i].append(candi[:idx] + candi[idx+1:])
        elif len(candi) < len_B:
            dp[i].append(candi[:idx] + B[idx] + candi[idx:])


            

