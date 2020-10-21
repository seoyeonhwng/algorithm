# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        p = head
        nums = []
        
        while p:
            nums.append(p.val)
            p = p.next
            
        nums.sort()
        
        p = head
        for n in nums:
            p.val = n
            p = p.next
            
        return head
        