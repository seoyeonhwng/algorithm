class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        def check(arr):
            return all(x<=y for x, y in zip(arr, arr[1:]))
        
        count = 0
        for c in range(len(A[0])):
            column = [A[i][c] for i in range(len(A))]
            if not check(column):
                count += 1
        return count

"""
[빠른 풀이]
- column이 정렬되어 있지 않다면 틀린 것!

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
    	return sum(list(i) != sorted(i) for i in zip(*A))
"""