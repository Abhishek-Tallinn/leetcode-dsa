# Problem: Leetcode 2413 - Smallest even multiple
# Difficulty: Easy
# Link: https://leetcode.com/problems/smallest-even-multiple/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We loop till 2*n as twice of n will definitely be divisible by 2 and n and we return the number
# as soon as we find that it is divisible by both 2 and n.

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(2,n*2+1):
            if i%2==0 and i%n==0:
                return i