# Problem link
https://leetcode.com/problems/climbing-stairs/

# Memoization solution
def helper(n,temp):
    # Base case
    if n==1:
        temp[n-1]=1
        return temp[n-1]
    elif n==2:
        temp[n-1]=2
        return temp[n-1]
    # Memoize
    if temp[n-1] is not None:
        return temp[n-1]
    # Choice diagram
    #Take one step
    temp[n-1]=helper(n-1,temp)+helper(n-2,temp)
    return temp[n-1]
class Solution:
    def climbStairs(self, n: int) -> int:
        temp=[None for _ in range(n+1)]
        helper(n,temp)
        return temp[n-1]

# Top down approach solution
class Solution:
    def climbStairs(self, n: int) -> int:
        temp=[None for _ in range(n+1)]
        for i in range(1,n+1):
            if i==1:
                temp[i]=1
            elif i==2:
                temp[i]=2
            else:
                temp[i]=temp[i-1]+temp[i-2]
        return temp[n]

