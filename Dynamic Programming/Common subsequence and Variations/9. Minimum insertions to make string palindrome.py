# Problem liink
'''
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
'''


def lcs(a, b):
    n = len(a)
    m = len(b)
    temp = [[None for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                temp[i][j] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                temp[i][j] = 1 + temp[i - 1][j - 1]
            else:
                temp[i][j] = max(temp[i - 1][j], temp[i][j - 1])
    return temp[n][m]


class Solution:
    def minInsertions(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        n = lcs(s, s[::-1])
        return len(s) - n
