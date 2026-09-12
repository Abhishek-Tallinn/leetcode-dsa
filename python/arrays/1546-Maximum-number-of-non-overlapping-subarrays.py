# Problem: Leetcode 1546 - Maximum number of non overlapping subarrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays/description/
# Time Complexity: O(n) as we save prefix sum in hashmap and keep updating them
# Space Complexity: O(n)
# Approach: We keep a running sum in hashmap and keep checking if the sum exists in hashmap and if it does we can update our left pointer 
# so that the overlapping arrays are not counter and we keep setting left = right as cutting at index at left meaning we are taking the subarray
# from index left + 1 to right as the prefix sum is taken from 0 to i

from collections import defaultdict
from typing import List
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        '''
        seen = {0}
        cnt = 0
        curr_sum=0
        for num in nums:
            curr_sum+=num
            if curr_sum-target in seen:
                seen = {0}
                curr_sum = 0
                cnt+=1
            else:
                seen.add(curr_sum)
        return cnt
        '''
        d = defaultdict(int)
        curr_sum = 0
        cnt = 0
        d[0]=-1
        left = -1
        for right in range(len(nums)):
            curr_sum+=nums[right]
            if curr_sum - target in d:
                if d[curr_sum-target]>=left:
                    cnt+=1
                    left = right
            
            d[curr_sum] = right
 
        return cnt
        