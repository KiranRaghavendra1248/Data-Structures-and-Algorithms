# Problem link
'''
https://leetcode.com/problems/target-sum/
'''
# Here, original plan would be to use Count num of subsets with given difference using Subset Sum
# As that is what is basically being done.
# Elements are being grouped into two subsets, such that diff of two subsets=S
# But that wont work here, as in Count num of subsets with given sum, we initialize first column to 1
# This is because, for any value of n, the only S=0 subset that can be formed is the empty subset i.e []
# But in this question, the values in the arr may contain 0. Hence that initialization will give a wrong answer
# This approach can be used only if zeros are not present in the array.
# Hence, this approach cannot be used.

# Here storing is a bit different
# Usually our temp is of shape [N+1][S+1]
# Here, on leetcode, constraint is given that, sum maybe max of 1000
# Hence, max and mix sum of the array are 1000 and -1000.
# Num of ways to attain sum=100 is stored at temp[N][100+1000]=temp[N][1100]
# Num of ways to attain sum=-100 is stored at temp[N][-100+1000]=temp[N][900]


# If remaining sum becomes 0, then our current path is 1 way to make given sum
# If we add a positive element, remaining sum i.e S decreases by value of the positive element
# If we add a negative element, remaining sum i.e S increase by value of the negative element

# Suppose S=998 and sum(arr)=999 and arr=[1,998]
# If we add negative element -998, S i.e remaining sum to be attained, increases to 1997
# While index accessing this element in temp: temp[N][1997+1000]=temp[N][2997] gives index error
# Hence shape of temp cant be [N+1][2001]
# Hence temp shape must be [N+1][S+2001]

# Temp storage is divided in this way
# Cols [0 to S+1000]- for when we add a positive element, and remaining S decreases by value added
# Cols [S+1000 to 2000 ]- for when we a negative element, and remaining S increases by negative value added

# Base condition initalization
# If remaining sum=0 and remaining elements=0 only then, we have found a path, as we have to include all the elements to make a sum.
# If remaining sum=0 and remaining elements!=0 or vice versa, that is not a valid path.


# Memoization approach
def helper(arr, S, N, temp):

    # Base case initialization
    if S == 0 and N == 0:
        return 1
    if N == 0:
        return 0
    # Memoization
    if temp[N][S + 1000] is not None:
        return temp[N][S + 1000]

    # Choice diagram
    # Each element can be added or subtracted
    add = helper(arr, S - arr[N - 1], N - 1, temp)
    subtract = helper(arr, S + arr[N - 1], N - 1, temp)
    temp[N][S + 1000] = add + subtract
    return temp[N][S + 1000]


class Solution:
    def findTargetSumWays(self, arr: List[int], S: int) -> int:
        N = len(arr)
        if sum(arr) < S:
            return 0
        # max value that sum(arr) might take = 1000 (positive of negative )
        temp = [[None for _ in range(S + 2001)] for _ in range(N + 1)]
        return helper(arr, S, N, temp)




