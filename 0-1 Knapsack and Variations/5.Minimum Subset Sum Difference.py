# Problem link
# GFG editor gives TLE for DP solution also
'''
https://practice.geeksforgeeks.org/problems/minimum-sum-partition3317/1
https://www.interviewbit.com/problems/minimum-difference-subsets/#
'''

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