# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def findTilt(self, root: TreeNode) -> int:
        def sub_find(node):
            if not node:
                return 0
            
            l = sub_find(node.left)
            r = sub_find(node.right)
            self.count += abs(l - r)
            
            return node.val + l + r
        
        sub_find(root)
        return self.count