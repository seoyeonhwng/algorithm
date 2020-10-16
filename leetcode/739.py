class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        
        for i, t in enumerate(T):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and t > stack[-1][1]:
                w_i, w_t = stack.pop()
                T[w_i] = i - w_i
            stack.append((i, t))
            
        while stack:
            i, t = stack.pop()
            T[i] = 0
            
        return T

"""
이런 문제는 가시화 꼭 해보자!!
"""