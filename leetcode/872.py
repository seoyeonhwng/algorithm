# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            path, stack = [], [node]
            
            while stack:
                v = stack.pop()
                if not v.left and not v.right:
                    path.append(v.val)
                    
                if v.left:
                    stack.append(v.left)
                if v.right:
                    stack.append(v.right)
            
            return path
                
        return dfs(root1) == dfs(root2)

"""
이 문제처럼 무언가 return해야 하는 상황이면 dfs를 스택버젼으로 구현하는 것이 더 직관적!
"""