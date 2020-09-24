class Solution:
    def decodeString(self, s: str) -> str:
        # ']' 일때 stack에서 pop하면서 계산을 시작한다!
        # - '['이 나올때까지 pop해서 문자열 만들고 숫자까지 처리 -> 다시 스택에!
        # 나머지는 stack에 푸쉬!
        stack = []
        
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                sub = ''
                while stack and stack[-1] != '[':
                    sub = stack.pop() + sub
                stack.pop() # '[' 처리
                
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * sub)
        
        return ''.join(stack)
                    
        