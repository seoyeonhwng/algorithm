class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = [i+1 for i in range(n)]
        answer, p = [], 0

        for a in arr:
            if p == len(target):
                return answer
            
            if a != target[p]:
                answer += ['Push', 'Pop']
            else:
                answer.append('Push')
                p += 1
     
        return answer
                