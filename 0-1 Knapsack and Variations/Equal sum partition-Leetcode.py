# Problem link
https://leetcode.com/problems/partition-equal-subset-sum/

# Here if we need to find 2 subsets of sum S, implies sum of total arr=2*S
# Hence, sum(arr)=2*S must be even. If it is odd return false.
# Further, we just need to find if a subset of sum=S=sum(arr)//2 exists.
# If it does,  all elements not in the first subset, will constitue of the other half of 2*S.
class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        if sum(arr)%2!=0:
            return False
        S=sum(arr)//2
        N=len(arr)
        temp=[[None for _ in range(S+1)] for _ in range(N+1)]
        # Base condition initialization
        for i in range(N+1):
            for j in range(S+1):
                if i==0:
                    temp[i][j]=False
                if j==0:
                    temp[i][j]=True
        # Choice diagram
        for i in range(1,N+1):
            for j in range(1,S+1):
                if arr[i-1]>j: # Bigger than remaining sum, hence it cant be included
                    temp[i][j]=temp[i-1][j]
                else:          # Now we have a choice to include or not
                    temp[i][j]=temp[i-1][j-arr[i-1]] or temp[i-1][j]
        return temp[N][S]