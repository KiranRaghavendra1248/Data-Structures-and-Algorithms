# Problem link
https://leetcode.com/problems/min-cost-climbing-stairs/

# Memoization approach
# Here helper(cost,N,temp) returns minimum cost to take last N steps.
def helper(cost, height, temp):
    # Base condition
    if height == 1:
        return cost[-1]
    if height == 2:
        return cost[-2]
    if temp[height] is not None:
        return temp[height]
    # Choice diagram
    temp[height] = cost[-height] + min(helper(cost, height - 1, temp), helper(cost, height - 2, temp))
    return temp[height]


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        height = len(cost)
        temp1 = [None for _ in range(height + 1)]
        temp2 = [None for _ in range(height + 1)]
        return min(helper(cost, height, temp1), helper(cost, height - 1, temp2))


# Top down approach
# Here temp[i] signifies, minimum cost to take last i steps.
# Hence temp[height] signifies min cost to take last N steps, i.e all steps i.e start from index 0
# temp[height-1] signifies min cost to take, last N-1 steps, i.e start from index 1
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        height=len(cost)
        temp=[None for _ in range(height+1)]
        # Base condition inititalization
        for i in range(1,height+1):
            if i==1:
                temp[i]= cost[-1]
            elif i==2:
                temp[i]= cost[-2]
            else:
        # Choice diagram
                temp[i]=cost[-i]+ min(temp[i-1],temp[i-2])
        return min(temp[height], temp[height-1])