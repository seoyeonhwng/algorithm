class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            if node == len(graph) - 1:
                answer.append(path)
                return
                
            for w in graphs[node]:
                if w not in path:
                    dfs(w, path + [w])
        
        graphs = {}
        for i, g in enumerate(graph):
            graphs[i] = g
        
        answer = []
        dfs(0, [0])
        return answer

"""
* 기본적인 DFS 문제 *
def dfs(v):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            dfs(w)
"""