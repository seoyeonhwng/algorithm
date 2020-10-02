# 맨처음에는 egg -> '011' 이렇게 string으로 바꿨는데 그렇게할 필요 없음!

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = collections.defaultdict(list)
        map_t = collections.defaultdict(list)
        
        for i, c in enumerate(s):
            map_s[c].append(i)
        
        for i, c in enumerate(t):
            map_t[c].append(i)
            
        return sorted(map_s.values()) == sorted(map_t.values())