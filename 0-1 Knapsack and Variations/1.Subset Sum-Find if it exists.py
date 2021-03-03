# Problem link
'''
https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
'''
# Here we have to return true if a subset of given sum exists, else return false
# Here temp[i][j] is True if sum of j can be made with first i numbers(by dropping some and selecting some)
# Hence the any true value in last row, signifies, all possible sums i.e js than can be made with n elements(i.e all elements)
# Top down approach
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