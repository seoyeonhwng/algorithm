class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        converted = []
        for a in A:
            converted.append([b^1 for b in a[::-1]])
        
        return converted