# Problem link
'''
https://leetcode.com/problems/longest-palindromic-substring/
'''
# Barely getting accepted, find new method
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        length = 0
        result = ''
        for end in range(len(s)):
            for start in range(end + 1):
                if start == end:
                    dp[start][end] = True
                elif start + 1 == end:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = s[start] == s[end] and dp[start + 1][end - 1]

                if dp[start][end] and end - start + 1 > length:
                    length = end - start + 1
                    result = s[start:end + 1]
        return result


