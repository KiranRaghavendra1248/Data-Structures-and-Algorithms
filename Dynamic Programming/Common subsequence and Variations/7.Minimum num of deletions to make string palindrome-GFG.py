# Problem link
'''
https://practice.geeksforgeeks.org/problems/minimum-deletitions1648/1
'''
# The deletions must be minimum and we must make it into palindrome.
# So basically we have to find, Len(S)-Len(Length of longest palindromic subsequence)
# This, will lead to minimum number of deletions
# Top down approach
class Solution:
    def minimumNumberOfDeletions(self,S):
        N=len(S)
        R=S[::-1]
        temp=[[None for _ in range(N+1)] for _ in range(N+1)]
        for i in range(N+1):
            for j in range(N+1):
                if i==0 or j==0:
                    temp[i][j]=0
        for i in range(1,N+1):
            for j in range(1,N+1):
                if S[i-1]==R[j-1]:
                    temp[i][j]=1+temp[i-1][j-1]
                else:
                    temp[i][j]=max(temp[i-1][j],temp[i][j-1])
        return(len(S)-temp[N][N])

# Bottom up approach
def helper(temp,S,R,N,M):
    if N==0 or M==0:
        return 0
    if temp[N][M] is not None:
        return temp[N][M]
    if S[N-1]==R[M-1]:
        temp[N][M]=1+helper(temp,S,R,N-1,M-1)
    else:
        temp[N][M]=max(helper(temp,S,R,N-1,M),helper(temp,S,R,N,M-1))
    return temp[N][M]
class Solution:
    def minimumNumberOfDeletions(self,S):
        N=len(S)
        R=S[::-1]
        temp=[[None for _ in range(N+1)] for _ in range(N+1)]
        return (N-helper(temp,S,R,N,N))