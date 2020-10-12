class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, sums = 1, 0
        
        while n > 0:
            q, r = divmod(n, 10)
            product *= r
            sums += r
            n = q
            
        return product - sums

"""
[빠른 풀이]
- 원소를 반복해서 계산하는 경우 Lambda + reduce!!!

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = [int(s) for s in str(n)]
        return reduce((lambda x, y: x*y), a) - reduce((lambda x,y: x+y), a)
"""