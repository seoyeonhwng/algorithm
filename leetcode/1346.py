class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        possible_n = set()
        possible_m = set()
        
        for a in arr:
            if a in possible_n:
                return True
            if a in possible_m:
                return True
            
            if a % 2 == 0:
                possible_m.add(a // 2)
            possible_n.add(a * 2)
        return False
"""
시간을 줄이기 위해서 
- 멤버십 체크는 set으로!
- index를 찾는대신 set 두개를 사용!
"""