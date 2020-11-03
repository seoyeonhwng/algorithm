class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squared = sorted([a ** 2 for a in A])
        return squared
        