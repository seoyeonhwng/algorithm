class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(elements):
            if prev_elements:
                result.add(''.join(prev_elements))
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
            
        result = set()
        prev_elements = []
        
        dfs(list(tiles))
        
        return len(result)

"""
[빠른 풀이]
- 문자열로 만들수 있는 모든 순열을 구하는 문제 -> DFS
- 같은 dfs 풀이여도 확실히 내 코드가 난잡하다..

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(path, t):
            if path:
                result.add(path)
                
            for i in range(len(t)):
                dfs(path + t[i], t[:i]+t[i+1:])
        
        result = set()
        dfs('', tiles)
        return len(result)
"""