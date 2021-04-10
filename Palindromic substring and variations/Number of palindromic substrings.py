# Problem link
'''
https://leetcode.com/problems/palindromic-substrings/
'''

# Here the shape of temp is N*N, where the vertical side represents, start index of the string and
# the horizontal side represents the y axis of the string.
# The table is filled in a diagonal manner
# First, all single length palindromes ar put True and counted
# Then, all two length palindromes are marked True or False and counted if its True
# The looping is similar to the loop in Matrix Chain Multiplication
# Length loops from 3 till N+1 i.e only till N
# i loops from 0 to N+1-Length i.e only till N-Length, i is the start index
# j=i+Length-1 is the end index
# For all strings from length 3 to N: If s[start-index]=s[end-index] and temp[i+1][j-1]=1,
# i.e the string leaving out the start and end index, i.e the inner string must be a palindrome.
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        temp = [[None for _ in range(N)] for _ in range(N)]
        # Base conditions
        # 1. All length one strings make palindromes
        ans = 0
        for i in range(N):
            temp[i][i] = 1
            ans += temp[i][i]
        for i in range(N - 1):
            temp[i][i + 1] = s[i] == s[i + 1]
            ans += temp[i][i + 1]
        for length in range(3, N + 1):
            for i in range(0, N + 1 - length):
                j = i + length - 1
                temp[i][j] = s[i] == s[j] and temp[i + 1][j - 1]
                ans += temp[i][j]
        return ans
