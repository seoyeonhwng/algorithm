class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        def get_change(wallet, money):
            if money == 0:
                return wallet
            
            # 가능한 잔돈 조합을 구해
            change = {}
            for unit in [20, 10, 5]:
                if wallet[unit] == 0:
                    continue
                count = min(wallet[unit], money//unit)
                change[unit] = count
                money -= count * unit
            
            # 가능하다면 잔돈 거스르고 남은 돈 리턴
            if money != 0:
                return None
   
            for k, v in change.items():
                wallet[k] -= v
            return wallet
           
                
        wallet = {20:0, 10:0, 5:0}
        for b in bills:
            wallet[b] += 1
            change = get_change(wallet, b - 5)
            
            if change is None:
                return False
            wallet = change
        return True

"""
[빠른 풀이]
- 잔돈이 5, 10밖에 없고 input도 제한적이므로 if-else문으로 처리하는 것이 더 빠름

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if five and ten:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
"""