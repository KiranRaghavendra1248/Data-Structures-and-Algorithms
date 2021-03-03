# Problem link
'''
https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1#
'''
# Top down approach
# Here, we have to return the count of subsets, of given sum
# User function Template for python3
class Solution:
    def perfectSum(self, arr, N, S):
        # code here
        temp = [[None for _ in range(S + 1)] for _ in range(N + 1)]

    # If i==0 i.e if num of elements=0, oly sum=0 can be produced, no other sum can be produced with array of 0 elements, so it is initialized to false
    # If j==0 i.e sum=0 can be produced by array of any num of elements by selecting an empty subset, so it is initialized to true.
    # Refer notes

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
                    temp[i][j] = temp[i - 1][j] % (10 ** 9 + 7)
                else:
                    # Now we have choice to include or not
                    # We add the two results
                    temp[i][j] = temp[i - 1][j - arr[i - 1]] % (10 ** 9 + 7) + temp[i - 1][j] % (10 ** 9 + 7)
        return (temp[N][S] % (10 ** 9 + 7))