class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = collections.Counter()
        for i, e in enumerate(list1):
            d1[e] = i
        
        d2 = collections.Counter()
        for i, e in enumerate(list2):
            d2[e] = i
            
        # 공통 원소!
        intersections = set(d1.keys()) & set(d2.keys())
        infos = {}
        min_value = sys.maxsize
        
        for inter in intersections:
            s = d1.get(inter) + d2.get(inter)
            infos[inter] = s
            min_value = min(min_value, s)
        
        result = []
        for key, value in infos.items():
            if value == min_value:
                result.append(key)
        return result

"""
[빠른 풀이]
- d2를 d1에 존재하는 키만 생성하는 것이 핵심!

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {e:i for i, e in enumerate(list1)}
        d2 = {e:i + d1[e] for i, e in enumerate(list2) if e in d1}
        
        result = []
        min_value = sys.maxsize
        
        for key, value in d2.items():
            if value < min_value:
                result = [key]
                min_value = value
            elif value == min_value:
                result.append(key)
                
        return result
"""