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
# Hence, this approach needs some modifications. Remove all zeros, n them proceed with same and at the end
# consider number of zeros and include the possible combinations that arises when all those zeros are included.
# 0 can be +0 or -0. Hence each 0 rises 2 combinations.

class Solution:
    def findTargetSumWays(self, arr: List[int], diff: int) -> int:
        S1=sum(arr)
        S=(diff+S1)/2
        if S!=int(S): # Make sure subset sum is an integer.
            return 0
        S=(diff+S1)//2
        arr_mod=[]
        count=0
        for i in arr:
            if i!=0:
                arr_mod.append(i)
            else:
                count+=1
        N=len(arr_mod)
        temp=[[None for _ in range(S+1)] for _ in range(N+1)]
        for i in range(0,N+1):
            for j in range(0,S+1):
                if i==0:
                    temp[i][j]=0
                if j==0:
                    temp[i][j]=1
        for i in range(1,N+1):
            for j in range(1,S+1):
                if arr_mod[i-1]>j:
                    temp[i][j]=temp[i-1][j]
                else:
                    temp[i][j]=temp[i-1][j]+temp[i-1][j-arr_mod[i-1]]
        for i in temp:
            print(i)
        return (2**count)*temp[N][S] # 2**count is the number of combination that rises from count number of 0s.



