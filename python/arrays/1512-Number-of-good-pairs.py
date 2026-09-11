# Problem: Leetcode 1512 - Number of good pairs
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-good-pairs/description/
# Time Complexity: O(n log n) due to sorting.
# Space Complexity: O(1) if we don't count the space used by the sorting algorithm although timsort uses some space internally in python.
# Approach: We can brute force with dual loops or we can store the freq of values in hashmap and then use the formuala n*(n-1)//2 to check 
# how many pairs does the occurence of this key make.


from collections import Counter
from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        d = Counter(nums)
        for v in d.values():
            cnt+= (v*(v-1))//2
        return cnt
        '''
        #brute force
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == nums[i]:
                    cnt+=1
        return cnt
        '''