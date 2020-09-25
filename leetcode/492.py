class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        q = area
        i = 1
        
        while q > i:
            i += 1
            if area % i == 0:
                q = area // i
            
        return [i, q]

"""
[빠른 풀이]
- center에 접근하기 위해 루트를 사용한다!!!!

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mid = int(math.sqrt(area))
        
        while area % mid != 0:
            mid -= 1

        return [int(area/mid),mid]

"""