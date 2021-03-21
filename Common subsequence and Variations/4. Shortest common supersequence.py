# Problem link
'''
https://practice.geeksforgeeks.org/problems/shortest-common-supersequence0322/1
'''
# Length of shortest common supersequence is given by M+N-(Longest common subsequence) as Longest common subsequence
# signifies the alphabets, which are common in both strings i.e appear twice in M+N, hence it must be subtracted once.
# Top down approach
def shortestCommonSupersequence(X, Y, N, M):
    temp = [[None for _ in range(M + 1)] for _ in range(N + 1)]
    # Base condition initialization
    for i in range(N + 1):
        for j in range(M + 1):
            if i == 0 or j == 0:
                temp[i][j] = 0
    # Choice diagram
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if X[i - 1] == Y[j - 1]:
                temp[i][j] = 1 + temp[i - 1][j - 1]
            else:
                temp[i][j] = max(temp[i - 1][j], temp[i][j - 1])
    return M + N - temp[N][M]