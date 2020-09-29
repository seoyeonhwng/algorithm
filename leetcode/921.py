class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if not S:
            return 0
        
        # 남은 스택의 개수!
        stack = []
        answer = 0
        
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                if not stack:
                    answer += 1
                else:
                    stack.pop()
                
        return len(stack) + answer
                    