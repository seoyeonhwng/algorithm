# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(root):
            stack, path = [root], []
            
            while stack:
                v = stack.pop()
                if not v:
                    path.append(None)
                else:
                    path.append(v.val)
                    stack.append(v.left)
                    stack.append(v.right)

            return path
        
        return dfs(p) == dfs(q)

"""
[빠른 풀이]
- dfs 방문 순서를 굳이 다 비교할 필요없이 재귀로 하나씩 비교하면 더 간단!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 둘 다 none이면 끝!
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
"""