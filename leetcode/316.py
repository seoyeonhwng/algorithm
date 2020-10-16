class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        
        stack = []
        seen = set()
        
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            
            # 뒤에 붙일 문자가 남아있다면 스택에서 제거
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)
            
        return ''.join(stack)