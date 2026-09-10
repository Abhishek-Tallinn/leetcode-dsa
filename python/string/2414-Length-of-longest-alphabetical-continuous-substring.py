# Problem: Leetcode 2414 - Length of longest alphabetical continuous substring
# Difficulty: Medium
# Link: https://leetcode.com/problems/length-of-longest-alphabetical-continuous-substring/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: we simply loop the string and check if substring can be extended. if yes we extend it and record the mx length and if no
# then we just set curr_len back to 1 which is the curr element which broke the previous sequence.

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        mx = 1
        curr_len = 1
        for i in range(1,len(s)):
            if ord(s[i]) - 1 == ord(s[i-1]):
                curr_len+=1
                mx = max(mx,curr_len)
            else:
                curr_len = 1
                
        return mx