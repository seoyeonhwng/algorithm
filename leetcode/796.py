class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        
        candidates = []
        for i, a in enumerate(A):
            if a == B[0]:
                candidates.append(i)
                
        for candi in candidates:
            rotated = A[candi:] + A[:candi]
            if rotated == B:
                return True
            
        return False