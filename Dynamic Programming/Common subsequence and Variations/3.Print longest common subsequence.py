# Can't seem to find problem link
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
        u = m
        v = n
        ans=''
        while u > 0 and v > 0:
            if X[u - 1] == Y[v - 1]:
                ans += X[u - 1]
                u -= 1
                v -= 1
            else:
                if temp[u - 1][v] > temp[u][v - 1]:
                    u = u - 1
                else:
                    v = v - 1
        print(ans[::-1])
