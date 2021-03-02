# Problem link
https://www.hackerearth.com/problem/algorithm/subset-sum-8/

N, S = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
temp = [[None for _ in range(S + 1)] for _ in range(N + 1)]


class Node:
    def __init__(self, n, s, l):
        self.n = n
        self.s = s
        self.l = l
# If i==0 i.e if num of elements=0, oly sum=0 can be produced, no other sum can be produced with array of 0 elements, so it is initialized to false
# If j==0 i.e sum=0 can be produced by array of any num of elements by selecting an empty subset, so it is initialized to true.
# Refer notes


# Base condition initialization
for i in range(N + 1):
    for j in range(S + 1):
        if i == 0:
            temp[i][j] = False
        if j == 0:
            temp[i][j] = True

# Choice diagram
for i in range(1, N + 1):
    for j in range(1, S + 1):
        if arr[i - 1] > j:  # We can't include as it is bigger
            temp[i][j] = temp[i - 1][j]
        else:
            # Now we have choice to include or not
            # We add the two results
            temp[i][j] = temp[i - 1][j - arr[i - 1]] or temp[i - 1][j]

# For printing the subsets, do a BFS from the last element. Two branches for each node is included and not included.
# Keep track of the path
# If it reaches beginning node, print out the path i.e put it somewhere so that it can be sorted and printed at the end
last_ele = Node(N, S, [])
q = []
q.append(last_ele)
result = []
while q:
    curr = q.pop(0)
    if curr.s == 0 and curr.n == 0:
        temp1 = curr.l.copy()
        temp1.sort()
        if temp1 not in result:
            result.append(temp1)
        continue
    # Excluded curr ele
    # If exclude variable is true, it signifies that current sum i.e curr.s can/has been attained by excluding the curr ele.
    # Hence we make a new node, by excluding the curr ele and add it to the queue
    exclude = temp[(curr.n) - 1][curr.s]
    if exclude:
        q.append(Node(curr.n - 1, curr.s, curr.l))
    # Included current element
    # If include variable is true, it signifies that current sum i.e curr.s can/has been attained by including the curr ele.
    # Hence we make a new node, by including the curr ele and reducing the remaining sum to be attained and add it to the queue
    # Only if Remaining required sum >= curr element value
    if curr.s >= arr[(curr.n) - 1]:
        include = temp[curr.n - 1][curr.s - arr[curr.n - 1]]
        if include:
            l = curr.l.copy()
            l.append(arr[curr.n - 1])
            q.append(Node(curr.n - 1, curr.s - arr[curr.n - 1], l))
result.sort()
for i in result:
    print(*i)




