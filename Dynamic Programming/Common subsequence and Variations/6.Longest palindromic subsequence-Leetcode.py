# Problem link
'''
https://leetcode.com/problems/longest-palindromic-subsequence/
'''
# Approach is, LCS of  reverse(s) & s is the longest palindromic subsequence
# Top down approach
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        sr=s[::-1]
        N=len(s)
        temp=[[None for _ in range(N+1)] for _ in range(N+1)]
        for i in range(N+1):
            for j in range(N+1):
                if i==0 or j==0:
                    temp[i][j]=0
        for i in range(1,N+1):
            for j in range(1,N+1):
                if s[i-1]==sr[j-1]:
                    temp[i][j]=1+temp[i-1][j-1]
                else:
                    temp[i][j]=max(temp[i-1][j],temp[i][j-1])
        return (temp[N][N])