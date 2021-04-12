# Problem link
'''
https://leetcode.com/problems/minimum-window-substring/
'''
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        formed = 0
        start = 0
        end = 0
        d1 = {}
        d2 = Counter(t)
        m = len(d2)
        minlen = 10 ** 6
        result = ''
        while end < n:
            char = s[end]
            d1[char] = d1.get(char, 0) + 1
            if char in d2:
                if d1[char] == d2[char]:
                    formed += 1
            while start <= end and formed == m:
                if end - start + 1 < minlen:
                    minlen = end - start + 1
                    result = s[start:end + 1]
                char = s[start]
                d1[char] -= 1
                if char in d2:
                    if d1[char] < d2[char]:
                        formed -= 1
                start += 1
            end += 1
        return result


