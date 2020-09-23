# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        curr = root
        stack = []
        result = []
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
            
        return result

# 중위 순회를 재귀로 하지 않는 경우 스택을 이용한다!
        