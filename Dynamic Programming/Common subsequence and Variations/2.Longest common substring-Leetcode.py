'''
https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1
'''
# Here, substring has to be continuous, so if a mismatch occurs, then temp[i][j] = 0
# When a match occurs, we increment the temp[i][j] prev continuous value and store its maximum
class Solution:
    def longestCommonSubstr(self, X, Y, n, m):
        temp=[[None for _ in range(m+1)] for _ in range(n+1)]
        # Base condition initialization
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0:
                    temp[i][j]=0
        # Choice diagram
        result=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if X[i-1]==Y[j-1]:
                    temp[i][j]=1+temp[i-1][j-1]
                    result=max(result,temp[i][j])
                else:
                    temp[i][j]=0
        return result