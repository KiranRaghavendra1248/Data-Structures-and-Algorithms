# Problem link
# GFG editor gives TLE for DP solution also
'''
https://practice.geeksforgeeks.org/problems/minimum-sum-partition3317/1
https://www.interviewbit.com/problems/minimum-difference-subsets/#
'''


class Solution:
    def solve(self, arr):
        # code here
        n=len(arr)
        S=sum(arr)
        temp=[[None for _ in range(S+1)] for _ in range(n+1)]
# First approach- My solution
# Here while looping, i signifies, num of elements left to choose from and j signifies, the sum left to be filled
# Base condition initialization:
# If j==0, i.e sum left to be filled is 0 i.e knapsack is full, i.e we have taken included all elements till the current i
# then curr_sum=sum till current i.
# Diff of this subset and the other is = abs(sum(arr[:i])-(S-sum(arr[:i])))
# If i==0, i.e num of elements to choose from becomes zero, curr_sum=j.
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

# Another approach( Comparitively easier)
# Run Subset sum for S=sum(arr), initialization n all same like subset sum
# Traverse thru last row of temp i.e i=N and find all true values
# For every true value, Sum of subset=j which implies, subset diff= j-(S-j)
# Among these, find the minimum one

# Here temp[i][j] is True if sum of j can be made with first i numbers(by dropping some and selecting some)
# Hence the any true value in last row, signifies, all possible sums i.e js than can be made with n elements(i.e all elements)
# But dont use this temp matrix populated with True or False for counting purpose
# For eg if temp[n][j]==True, it means, that j sum can be made using first n numbers in arr. But it doesnt tell, how many such subsets can be made.
def SubsetSum(arr, N, S):
    # code here
    temp = [[None for _ in range(S + 1)] for _ in range(N + 1)]

    # Base condition initialization
    for i in range(N + 1):
        for j in range(S + 1):
            if i == 0:
                temp[i][j] = False
            if j == 0:
                temp[i][j] = True

    # Choice diagram
    for i in range(1, N + 1):
        for j in range(1, S + 1):
            if arr[i - 1] > j:  # We can't include as it is bigger
                temp[i][j] = temp[i - 1][j]
            else:
                # Now we have choice to include or not
                # We add the two results
                temp[i][j] = temp[i - 1][j - arr[i - 1]] or temp[i - 1][j]
    return (temp)


class Solution:
    def minDiffernce(self, arr, n):
        # code here
        S = sum(arr)
        result = None
        temp = SubsetSum(arr, n, S)
        for i in range(len(temp[n])):
            if temp[n][i]:
                curr_sum = i
                subset_diff = abs(i - (S - i))
                if result is None:
                    result = subset_diff
                else:
                    result = min(result, subset_diff)
        return result