# Problem link
'''
https://leetcode.com/problems/coin-change-2/
'''


# Top down approach
class Solution:
    def change(self, M: int, coins: List[int]) -> int:
        N = len(coins)
        temp = [[None for _ in range(M + 1)] for _ in range(N + 1)]
        # Base condition initialization
        for i in range(N + 1):
            for j in range(M + 1):
                if i == 0:
                    temp[i][j] = 0
                if j == 0:
                    temp[i][j] = 1
        # Choice diagram
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if coins[i - 1] > j:  # Bigger, hence we can't include
                    temp[i][j] = temp[i - 1][j]
                else:
                    temp[i][j] = temp[i][j - coins[i - 1]] + temp[i - 1][j]
        return temp[N][M]


