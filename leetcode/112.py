# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = False
    def hasPathSum(self, root: TreeNode, s: int) -> bool:
        def dfs(node, path):
            if not node.left and not node.right:
                if sum(path) == s:
                    self.answer = True
                return
            
            if node.left:
                dfs(node.left, path + [node.left.val])
            if node.right:
                dfs(node.right, path + [node.right.val])
        
        if not root:
            return False
        
        dfs(root, [root.val])
        return self.answer
                
                    
            
            