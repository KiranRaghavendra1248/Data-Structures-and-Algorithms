# Problem link
'''
https://leetcode.com/problems/permutation-in-string/
'''
# Fixed length sliding window problem


def zero():
    return 0

from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        d2 = Counter(s2[:m])
        d1 = defaultdict(zero)
        for i in s1:
            d1[i] += 1
        for i in range(0, n - m + 1):
            # print(s2[i:i+m],d1,d2)
            flag = 0
            for key in d2:
                if d2[key] == d1[key]:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                return True
            if i + m < n:
                d2[s2[i]] -= 1
                d2[s2[i + m]] += 1
        return False




