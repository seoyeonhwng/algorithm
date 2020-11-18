class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        def toggle(arr):
            return [0 if a == 1 else 1 for a in arr]
        
        # 각 row의 첫번째가 0이면 toggle
        tmp = []
        for row in A:
            if row[0] == 0:
                tmp.append(toggle(row))
            else:
                tmp.append(row)
        
        # 각 col에서 0이 더 많으면 toggle
        rotated = []
        for col in zip(*tmp):
            if len(col)//2 >= sum(col):
                rotated.append(toggle(col))
            else:
                rotated.append(list(col))
                
        answer = 0
        for row in zip(*rotated):
            answer += int(''.join([str(r) for r in row]), 2)
   
        return answer