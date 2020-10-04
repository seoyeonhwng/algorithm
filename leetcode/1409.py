class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i+1 for i in range(m)]
        result = []
        
        for q in queries:
            # P에서 q의 index를 찾아 -> result에 저장
            pos = P.index(q)
            result.append(pos)
            # q를 P에서 맨 앞으로 이동
            P = [P[pos]] + P[:pos] + P[pos+1:]
        
        return result

"""
** q를 P 맨 앞으로 이동할때 슬라이싱하는 것 보다 insert & pop 이용하는 것이 더 빠름!

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i+1 for i in range(m)]
        result = []
        
        for q in queries:
            pos = P.index(q)
            result.append(pos)
            P.insert(0, P[pos])
            P.pop(pos+1)
    
        return result
"""