# Problem link
'''
https://leetcode.com/problems/coin-change/submissions/
'''
# Top down approach
# Here, initialization is a bit different from usual unbounded knapsack problems.
# For i=0,i.e n=0, for all sum=S, we initialize to infinity.
# For i=1, i.e we have only the 1st element to choose from, if amt%coins[0]==0, it is divisible.
# So this coin must be taken repeatedly to form amt.
# For j=0 i.e S=0, for all values of n, we initialize to 0.
# So, temp[i][j] stores the min num of coins needed to form sum/amt j, where we have i coins to choose from.
import sys
class Solution:
    def coinChange(self, coins: List[int], S: int) -> int:
        N = len(coins)
        MAX = sys.maxsize
        temp = [[None for _ in range(S + 1)] for _ in range(N + 1)]
        # Base condition
        for i in range(N + 1):
            for j in range(S + 1):
                if j == 0:
                    temp[i][j] = 0
                if i == 0:
                    temp[i][j] = MAX - 1
                if i == 1:
                    if j % coins[0] == 0:
                        temp[i][j] = j // coins[0]
                    else:
                        temp[i][j] = MAX - 1
        # Choice diagram
        for i in range(2, N + 1):
            for j in range(1, S + 1):
                if coins[i - 1] > j:  # Bigger hence, we cant include
                    temp[i][j] = temp[i - 1][j]
                else:  # We have an option to include or not, depending on which gives min coins
                    temp[i][j] = min(1 + temp[i][j - coins[i - 1]], temp[i - 1][j])
        if temp[N][S] == MAX - 1:
            return -1
        else:
            return temp[N][S]


