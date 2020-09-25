class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        left = 0
        right = 0
        result = []
        
        while left < len(s) and left <= right:
            # expand right
            while right < len(s) and s[left] == s[right]:
                right += 1
            
            if right - left >= 3:
                result.append([left, right - 1])
            
            left, right = right, right + 1
            
        return result
                
                