# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = [[root, None, None]]
        answer = 0
        
        while stack:
            v, parent, grand = stack.pop()
            if grand and grand.val % 2 == 0:
                answer += v.val
            
            if v.left:
                stack.append([v.left, v, parent])
            if v.right:
                stack.append([v.right, v, parent])
        
        return answer

"""
grand parent 노드의 값이 필요하므로 parent, grand parent를 계속해서 기억한다!!!
"""