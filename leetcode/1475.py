# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def is_palindrome(self, nums):
        counter = collections.Counter(nums)
        odd = 0
        for k in counter.keys():
            if counter[k] % 2 != 0:
                odd += 1
        
        return odd <= 1
      
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def dfs(node, path):
            if not node.left and not node.right: # leaf
                if self.is_palindrome(path + [node.val]):
                    self.count += 1
                return
            
            if node.left:
                dfs(node.left, path + [node.val])
            if node.right:
                dfs(node.right, path + [node.val])
           
        result = []
        dfs(root, [])
        
        return self.count