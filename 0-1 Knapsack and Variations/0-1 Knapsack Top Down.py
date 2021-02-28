def knapSack(W, wt, val, n):
    temp = [[None for _ in range(W + 1)] for _ in range(n + 1)]
    # Base condition initialization
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                temp[i][j] = 0

    # j signifies the weight that can be added/remaining wait in every iteration
    # i signifies, the num of elements left to choose from

    ## Choice Diagram
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if wt[i - 1] > j:  # Do not include,as its bigger
                temp[i][j] = temp[i - 1][j]
            elif wt[i - 1] <= j:  # Not bigger, but we have choice to include or not
                temp[i][j] = max(val[i - 1] + temp[i - 1][j - wt[i]], temp[i - 1][j])
    return temp[n][W]