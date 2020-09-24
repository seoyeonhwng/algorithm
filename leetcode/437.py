# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def pathSum(self, root: TreeNode, target: int) -> int:
        def dfs(node, path): 
            if not node:
                return
            
            if sum(path) == target:
                self.count += 1
            
            if node.left:
                dfs(node.left, path + [node.left.val])
            if node.right:
                dfs(node.right, path + [node.right.val])
        
        
        if not root:
            return 0
        
        stack = [root]
        while stack:
            v = stack.pop()
            dfs(v, [v.val])
            if v.left:
                stack.append(v.left)
            if v.right:
                stack.append(v.right)
                
        return self.count
            