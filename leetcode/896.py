class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = [False] * (len(A) - 1)
        decreasing = [False] * (len(A) - 1)
        
        for i in range(len(A)-1):
            if A[i] <= A[i+1]:
                increasing[i] = True
            if A[i] >= A[i+1]:
                decreasing[i] = True
                
        if all(increasing) or all(decreasing):
            return True
        return False