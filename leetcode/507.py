class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 약수 찾을때 루트num 까지만 찾아도 된다!
        if num == 1:
            return False
        
        count = 1
        i = 2
        
        while True:
            q, r = divmod(num, i)
            if i > q:
                break
                
            if r == 0:
                count += (i + q)
            i += 1
            
        return count == num
            