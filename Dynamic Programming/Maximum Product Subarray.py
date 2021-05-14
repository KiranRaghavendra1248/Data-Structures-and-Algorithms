# Problem link
'''
https://leetcode.com/problems/maximum-product-subarray/
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = minp = totalmax = nums[0]
        for i in range(1, len(nums)):
            temp = maxp
            maxp = max(nums[i], nums[i] * maxp, nums[i] * minp)
            minp = min(nums[i], nums[i] * temp, nums[i] * minp)
            totalmax = max(totalmax, maxp)
        return totalmax
