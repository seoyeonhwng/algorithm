# brute-force
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                for k in range(j+1, len(rating)):
                    if rating[i] < rating[j] < rating[k]:
                        count += 1
                    elif rating[i] > rating[j] > rating[k]:
                        count += 1
        
        return count

"""
* pivot을 중심으로 왼쪽, 오른쪽을 나눠서 생각한다 *
1) 왼쪽, 오른쪽에서 각각 pivot보다 큰 원소 개수, 작은 원소 개수 구한다
2)오름차순 경우의 수는 왼쪽 작은 * 오른쪽 큰
3) 내림차순 경우의 수는 왼쪽 큰 * 오른쪽 작은 

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        answer = 0
        
        for j in range(1, len(rating)-1):
            x, ll, hl, lr, hr = rating[j], 0, 0, 0, 0
            
            for i in range(j): # left
                if rating[i] > x:
                    hl += 1
                else:
                    ll += 1
            
            for k in range(j+1, len(rating)): # right
                if rating[k] > x:
                    hr += 1
                else:
                    lr += 1
                    
            answer += (ll * hr) + (hl * lr)
            
        return answer
"""