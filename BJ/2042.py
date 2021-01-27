from math import *

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)

    return tree[node]

def query(node, start, end, left, right):
    if left > end or start > right:
        return 0
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node*2, start, mid, index, diff)
        update(node*2+1, mid+1, end, index, diff)

N, M, K = map(int, input().split(' '))
height = ceil(log2(N))
tree_size = 1 << (height + 1) # 노드의 전체 개수 = 2 ^ (height + 1)
tree = [0] * tree_size

arr = []
for _ in range(N): # 리프 노드에 데이터 입력받기
    arr.append(int(input()))

init(1, 0, N-1)

for _ in range(M + K):
    a, b, c = map(int, input().split(' '))
    if a == 1: # update
        diff = c - arr[b-1]
        arr[b-1] = c
        update(1, 0, N-1, b-1, diff)
    else: # query
        print(query(1, 0, N-1, b-1, c-1))
