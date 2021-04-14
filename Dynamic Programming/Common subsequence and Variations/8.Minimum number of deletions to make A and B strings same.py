# Problem link
'''
https://leetcode.com/problems/delete-operation-for-two-strings/
'''
# The approach is to reduce both strings X and Y to its LCS(X,Y)
# And find out, how many chars must be deleted either from X or Y for this to happen
class Solution:
    def minDistance(self, X: str, Y: str) -> int:
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
        result=abs(len(X)-temp[N][M])+abs(temp[N][M]-len(Y))
        return result