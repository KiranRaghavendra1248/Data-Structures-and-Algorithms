# Problem link
# GFG editor gives TLE for DP solution also
https://practice.geeksforgeeks.org/problems/minimum-sum-partition3317/1
https://www.interviewbit.com/problems/minimum-difference-subsets/#


class Solution:
    def solve(self, arr):
        # code here
        n=len(arr)
        S=sum(arr)
        temp=[[None for _ in range(S+1)] for _ in range(n+1)]

# Here while looping, i signifies, num of elements left to choose from and j signifies, the sum left to be filled
# Base condition initialization:
# If j==0, i.e sum left to be filled is 0 i.e knapsack is full, i.e we have taken included all elements till the current i
# then curr_sum=sum till current i.
# Diff of this subset and the other is = abs(sum(arr[:i])-(S-sum(arr[:i])))
# If i==0, i.e num of elements to choose from becomes zero, curr_sum=if j:
# Diff of 2 subsets is = abs(j-(S-j)), where S=sum(arr)

        for i in range(n+1):
            for j in range(S+1):
                if j==0:
                    # If remaining sum=0, then for given i, all elements have been included
                    temp[i][j]=abs(sum(arr[:i])-(S-sum(arr[:i])))
                if i==0:
                    # If num elements=0, min diff=0 obviously
                    temp[i][j]=abs(j-(S-j))
        for i in range(1,n+1):
            for j in range(1,S+1):
                if arr[i-1]>j: # Big hence cant be included
                    temp[i][j]=temp[i-1][j]
                else: # We have a choice
                    temp[i][j]=min(temp[i-1][j],temp[i-1][j-arr[i-1]])
        return temp[n][S]