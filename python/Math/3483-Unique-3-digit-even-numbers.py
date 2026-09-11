# Problem: Leetcode 3483- unique 3 digit even numbers
# Difficulty: Easy
# Link: https://leetcode.com/problems/unique-3-digit-even-numbers/description/
# Time Complexity: O(n^3) for enumeration and O(1) for hashmap approach
# Space Complexity: O(1)
# Approach1: We can brute force with O(n^3) where we try every available digit in hundreds place except 0 and for each digit we take a tens digit and unit digit
# and keep counting the unique numbers found. 
# Approach2: We can do an efficient hashmap approach also which is O(1) as it has fixed 450 iterations where we loop over all the digits for the three place and check 
# if the number we arrived at can be made by the available digits. At every step we check how many copies of a digit we need and if we dont have enough we skip to next iteration
# and if we do then we go deeper to find the last digit for these numbers and if a number is possible we increment our count
# we return count at the end

from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        #efficient hashmap approach
        cnt = [0] * 10
        total = 0
        for d in digits:
            cnt[d]+=1
        for h in range(1,10):
            if cnt[h]==0:
                continue
            for t in range(10):
                need_t = (1 if t == h else 0)
                if cnt[t] <= need_t:
                    continue
                for u in range(0,10,2):
                    need_u = (1 if u==t else 0) + (1 if u==h else 0)
                    if cnt[u] <= need_u:
                        continue
                    total+=1
        return total
            
        '''
        #brute forcing O(n^3)
        seen = [False]*1000
        cnt = 0
        for h in range(len(digits)):
            if digits[h]==0:
                continue
            for t in range(len(digits)):
                if t == h:
                    continue
                for o in range(len(digits)):
                    if o == t or o == h or digits[o]%2!=0:
                        continue
                    temp = digits[h]*100+digits[t]*10+digits[o]
                    if not seen[temp]:
                        seen[temp] = True
                        cnt+=1
        return cnt
        '''



        '''enumerate approach
        unique = set()
        for unit_index, unit_digit in enumerate(digits):
            if unit_digit & 1:
                continue
            for tens_index,tens_digit in enumerate(digits):
                if tens_index == unit_index:
                    continue
                for hundred_index,hundred_digit in enumerate(digits):
                    if hundred_digit == 0 or hundred_index in (unit_index, tens_index):
                        continue
                    unique.add(hundred_digit*100+tens_digit*10+unit_digit)
        return len(unique)
        '''