# Problem: Leetcode 2404 - Most frequent even element
# Difficulty: Easy
# Link: https://leetcode.com/problems/most-frequent-even-element/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use a counter hashmap
# Approach: We avoid sorting and go through the hashmap and if a key has even value we compare its freq to the max freq seen till now
# and update max and take key in ans. If current key freq is equal to max then we update ans if key value is smaller than answer 
# so that we get the smallest number

from typing import List
from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = Counter(nums)
        mx = 0
        ans = -1
        for k,v in d.items():
            if k%2==0:
                if mx< v:
                    mx = v
                    ans = k
                elif mx==v:
                    if k < ans:
                        ans = k
        return ans