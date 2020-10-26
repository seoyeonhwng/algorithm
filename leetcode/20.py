class Solution:           
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                # char = 닫힘
                if not stack:
                    return False
                
                top = stack.pop()
                
                if top == '(':
                    answer = ')'
                elif top == '{':
                    answer = '}'
                elif top == '[':
                    answer = ']'
                
                if char != answer:
                    return False
        
        if stack:
            return False
        return True
            