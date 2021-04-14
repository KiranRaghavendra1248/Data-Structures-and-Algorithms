# Problem link
'''
https://leetcode.com/problems/longest-common-subsequence/
'''

# Memoization approach

def helper(s1,n,s2,m,temp):
    # Base condition initialization
    if n==0 or m==0:
        return 0
    if temp[n][m] is not None:
        return temp[n][m]
    # Choice diagram
    # If last alphabet matches, increment count by 1 and make recursive call for smaller s1 and smaller s2
    if s1[n-1]==s2[m-1]:
        temp[n][m]= 1+helper(s1,n-1,s2,m-1,temp)
    # Else, make recursive call leaving out the last alphabet in s1 the first time,
    # and leaving out the last alphabet in s2 the second time and store the max value of the two
    else:
        temp[n][m]=max( helper( s1,n-1,s2,m,temp), helper(s1,n,s2,m-1,temp) )
    return temp[n][m]
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n=len(s1)
        m=len(s2)
        temp=[[None for _ in range(m+1)] for _ in range(n+1)]
        return helper(s1,n,s2,m,temp)

# Top down approach
class Solution:
    def longestCommonSubsequence(self, X: str, Y: str) -> int:
        N=len(X)
        M=len(Y)
        temp=[[None for _ in range(M+1)] for _ in range(N+1)]
        # Base condition initialization
        for i in range(N+1):
            for j in range(M+1):
                if i==0 or j==0:
                    temp[i][j]=0
        # Choice diagram
        for i in range(1,N+1):
            for j in range(1,M+1):
                if X[i-1]==Y[j-1]:
                    temp[i][j]=1+temp[i-1][j-1]
                else:
                    temp[i][j]=max(temp[i-1][j],temp[i][j-1])
        return temp[N][M]