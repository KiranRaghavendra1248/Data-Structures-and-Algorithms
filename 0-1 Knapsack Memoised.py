def helper(W, wt, val, n, temp):
    if n == 0 or W == 0:
        return 0
    if temp[n][W] is not None:
        return temp[n][W]  # Memoization
    if wt[n - 1] > W:
        temp[n][W] = helper(W, wt, val, n - 1, temp)  # Storing
        return temp[n][W]
    elif wt[n - 1] <= W:
        temp[n][W] = max((val[n - 1] + helper(W - wt[n - 1], wt, val, n - 1, temp)),
                         helper(W, wt, val, n - 1, temp))  # Storing
        return temp[n][W]


def knapSack(W, wt, val, n):
    temp = [[None for _ in range(W + 1)] for _ in range(n + 1)]
    result = helper(W, wt, val, n, temp)
    return result