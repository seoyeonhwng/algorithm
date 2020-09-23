class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        queue = collections.deque(popped)
        stack = []
        
        for p in pushed:
            if p != queue[0]: # pop할 대상이 아니면 push
                stack.append(p)
            else:
                queue.popleft() # p 처리
                while stack and stack[-1] == queue[0]:
                    queue.popleft()
                    stack.pop()
                    
        if stack:
            return False
        return True