# Problem link
'''
https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1
'''
# Solution is similar to 0-1 Knapsack. If we include an item, we can include it again.
# If we dont, include it the first time, we can be sure that we wont be including it anytime again.
# so, if we include the Nth element, the next fun call, will again be on N, but weight reduced.
# If we dont include the element, the next fun call, will be pn N-1 with weight remaining to be same.

# Memoization approach
def helper(temp, N, W, val, wt):
    # Base condition initialization
    if N == 0 or W == 0:
        return 0
    # Memoize
    if temp[N][W] is not None:
        return temp[N][W]

    if wt[N - 1] > W:  # Bigger hence we cant include
        temp[N][W] = helper(temp, N - 1, W, val, wt)
    else:  # We have option to include or not
        temp[N][W] = max(val[N - 1] + helper(temp, N, W - wt[N - 1], val, wt), helper(temp, N - 1, W, val, wt))
    return temp[N][W]


class Solution:
    def knapSack(self, N, W, val, wt):
        temp = [[None for _ in range(W + 1)] for _ in range(N + 1)]
        return helper(temp, N, W, val, wt)

# Top down approach
class Solution:
    def knapSack(self, N, W, val, wt):
        temp=[[None for _ in range(W+1)]for _ in range(N+1)]
        # Base condition initialzation
        for i in range(N+1):
            for j in range(W+1):
                if i==0 or j==0:
                    temp[i][j]=0
        # Choice diagram
        for i in range(1,N+1):
            for j in range(1,W+1):
                if wt[i-1]>j: # Bigger hence we cant include
                    temp[i][j]=temp[i-1][j]
                else: # We have a choice
                    temp[i][j]=max(val[i-1]+temp[i][j-wt[i-1]],temp[i-1][j])
        return temp[N][W]
