# Problem link
# TLE fr python3 in GFG, editor problem, use leetcode link
'''
https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1
https://leetcode.com/problems/delete-operation-for-two-strings/
'''
# Top down approach
# We cant convert X to Y directly. What we do is  we convert X to LCS(X,Y) 
# and then convert LCS(X,Y) to Y

class Solution:
	def minOperations(self, X, Y):
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