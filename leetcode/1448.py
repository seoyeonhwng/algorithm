# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0
    def goodNodes(self, root: TreeNode) -> int:
        # path에 node보다 큰 값이 없다면 count + 1
        def dfs(node, path):
            if all([p <= node.val for p in path]):
                self.answer += 1
                
            if node.left:
                dfs(node.left, path + [node.val])
            if node.right:
                dfs(node.right, path + [node.val])
         
        dfs(root, [])
        return self.answer

"""
[빠른 풀이]
- 모든 path를 다 기억할 필요 없다! max값만 갱신하자!!!!!!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_v):
            if node.val >= max_v:
                self.answer += 1
                
            if node.left:
                dfs(node.left, max(max_v, node.val))
            if node.right:
                dfs(node.right, max(max_v, node.val))
         
        dfs(root, -sys.maxsize)
        return self.answer
"""