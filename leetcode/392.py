class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        queue = collections.deque(s)
        
        for char in t:
            if queue and queue[0] == char:
                queue.popleft()
                
        return not len(queue)