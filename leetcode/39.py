class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(path):
            c_sum = sum(path)
            if c_sum > target:
                return
            
            if c_sum == target:
                result.append(path)
                return
            
            for c in candidates:
                if path and c < path[-1]:
                    continue
                dfs(path + [c])
                
        result = []
        dfs([])
        
        return result