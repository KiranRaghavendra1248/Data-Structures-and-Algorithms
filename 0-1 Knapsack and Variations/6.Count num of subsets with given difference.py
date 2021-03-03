# Cant find the problem link/article anywhere
# Problem statement:
# Given an array arr and Difference D, find the num of subset pairs, whose difference=D


# The below fun returns num of subsets with sum=S i.e given sum
def CountSubsetswithSum(arr, N, S):
    # code here
    temp = [[None for _ in range(S + 1)] for _ in range(N + 1)]

    # Base condition initialization
    for i in range(N + 1):
        for j in range(S + 1):
            if i == 0:
                temp[i][j] = 0
            if j == 0:
                temp[i][j] = 1

    # Choice diagram
    for i in range(1, N + 1):
        for j in range(1, S + 1):
            if arr[i - 1] > j:  # We can't include as it is bigger
                temp[i][j] = temp[i - 1][j]
            else:
                # Now we have choice to include or not
                # We add the two results
                temp[i][j] = temp[i - 1][j - arr[i - 1]] + temp[i - 1][j]
    return (temp[N][S] )

# If S1 is sum of 1st subset and S2 is the sum of 2nd subset, then, S1+S2=S and S1-S2=D
# This implies S1=(S+D)/2
# So, now we need to find count of subsets with given sum=S1
def SubsetsWithDiffD(arr,D,n):
    # The range of subset sum=(0,sum(arr))
    S=sum(arr)
    S1 = (S + D) / 2
    return CountSubsetswithSum(arr, n, S1)

# Note
# But dont try to use temp matrix populated with True or False for counting purpose
# You can think of traversing the last row of the temp matrix, and finding what all
# subsets sums are possible with first n numbers(i.e the whole array), and check if any of them will have given Subset Diff
# But it doesnt give an indication of how many such subsets are possible.
# Hence, the answer returned will always be 1.
# For eg if temp[n][j]==True, it means, that j sum can be made using first n numbers in arr. But it doesnt tell, how many such subsets can be made.
