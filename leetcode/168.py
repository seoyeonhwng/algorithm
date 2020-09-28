class Solution:
    def convertToTitle(self, n: int) -> str:
        # 26진수!
        column = ''
        
        while n > 26:
            q, r = divmod(n, 26)
            n = q
          
            if r == 0:
                r = 26
                n -= 1
            column += chr(ord('A') + r - 1)
           
        
        column += chr(ord('A') + n - 1)
        return column[::-1]