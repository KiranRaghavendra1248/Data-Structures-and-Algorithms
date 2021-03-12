# Problem link
'''
https://www.geeksforgeeks.org/cutting-a-rod-dp-13/
'''

# Memoization approach
# Here, N is similar to W. length is similar to wt[] i.e we can choose
# any lengths to cut, such that total lengths cut does not exceed n
# And price[] is similar to val[] which must be maximized

def helper( temp, length, price, N, S):
    # Base condition initialization
    if N==0 or S==0:
        return 0
    if temp[N][S] is not None:
        return temp[N][S]
    # Choice diagram
    if length[S-1]>=S: # Cut cant be made and must be kept whole
        temp[N][S]=price[S-1]
    else: # We have a choice, to make a cut of length[N-1] rn or not
        temp[N][S]=max(price[N-1]+helper(temp,length,price,N,S-length[S-1]),helper(temp,length,price,N-1,S))
    return temp[N][S]



def cuttingrod(price, N):
    S=N
    temp=[None for _ in range(S+1) for _ in range(N+1)]
    length=[i for i in range(1,N+1)]
    return helper(temp,length,price,N,S)

# Top down approach
def cuttingrod(price,N):
    S=N
    temp = [None for _ in range(S + 1) for _ in range(N + 1)]
    length = [i for i in range(1, N + 1)]
    # Base condition initialization
    for i in range(N+1):
        for j in range(S+1):
            if i==0 or j==0:
                temp[i][j]=0
    # Choice diagram
    for i in range(1,N+1):
        for j in range(1,S+1):
            if length[i-1]>j: # Bigger hence, can't be included i.e cut can't be made
                temp[i][j]=temp[i-1][j]
            else: # We have option to make the cut or not
                temp[i][j]=max(price[i-1]+temp[i][j-price[i-1]],temp[i-1][j])
    return temp[N][S]





