class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        queue = collections.deque(piles)
        answer = 0
        
        while queue:
            queue.pop() # Alice
            answer += queue.pop() # me
            queue.popleft() # Bob
            
        return answer

"""
'내가 많이 가질려면 3개를 어떻게 뽑아야 하는가!'를 생각하는 것이 핵심
"""