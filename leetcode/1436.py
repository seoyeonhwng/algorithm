class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # start에는 있고 end에는 없다
        start, end = set(), set()
        
        for path in paths:
            start.add(path[0])
            end.add(path[1])
        
        return (end-start).pop()
