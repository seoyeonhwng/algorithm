# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, path):
            if not node.left and not node.right:
                result.append(path)
                return
            
            if node.left:
                dfs(node.left, path + '->' + str(node.left.val))
            if node.right:
                dfs(node.right, path + '->' + str(node.right.val))
        
        if not root:
            return []
        
        result = []
        dfs(root, str(root.val))
        return result