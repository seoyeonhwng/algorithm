# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder.pop(0))
        stack = [root]
        
        for p in preorder:
            node = TreeNode(p)
            if stack[-1].val > node.val:
                stack[-1].left = node
            else:
                while stack and stack[-1].val < node.val:
                    prev = stack.pop()
                prev.right = node
            stack.append(node)
            
        return root

"""
- stack을 떠올리기는 했는데 이렇게 노드 자체를 넣을 생각을 못함....
- 아이디어는 늘 간단하다!
- preorder를 돌면서 해당 숫자가 왼쪽 자식인지 오른쪽 자식인지 값을 비교하면서 넣어준다
"""