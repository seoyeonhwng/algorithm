class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

"""
* N이 짝수일때 Alice가 이기는 경우, 홀수일때 Alice가 이기는 경우로 나눠서 생각하는 아이디어!
"""