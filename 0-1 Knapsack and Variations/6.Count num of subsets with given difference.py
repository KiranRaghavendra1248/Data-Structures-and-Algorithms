# Cant find the problem link/article anywhere
# Problem statement:
# Given an array arr and Difference D, find the num of subset pairs, whose difference=D

def SubsetSum(arr,S,temp,N):
# Original subset sum function, which return True, if a subset of given sum is present.
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
    return (temp[N][S])
def SubsetsWithDiffD(arr,D,n):
    # The range of subset sum=(0,sum(arr))
    S=sum(arr)
    temp=[[None for _ in range(S+1)] for _ in range(n+1)]
    SubsetSum(arr,S,temp,n)
    # We use the SubsetSum function to populate the temp array.
    # In the last row of temp, if temp[i][j]=True, then a subset of sum j can be made from n elements(i.e all elements in the arr)
    # Using this, we get all possible subset pair differnces
    count=0
    for i in range(len(temp[n])):
        if temp[n][i]:
            curr_sum=j
            diff=abs(curr_sum-(S-curr_sum))
            if diff==D:
                count+=1
    return count