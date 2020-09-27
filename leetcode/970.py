class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2:
            return []
        
        if x == 1:
            candi_x = [1]
        else:
            i = 1
            candi_x = []
            while i < bound:
                candi_x.append(i)
                i *= x
        
        if y == 1:
            candi_y = [1]
        else:
            i = 1
            candi_y = []
            while i < bound:
                candi_y.append(i)
                i *= y
        
        result = set()
        for a in candi_x:
            for b in candi_y:
                if a + b <= bound:
                    result.add(a + b)
                    
        return result
            