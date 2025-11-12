from typing import List

class Solution:
    def minOperations(self, nums: List[int]):
        # Edge case where there is at least one 1 in the array
        n = len(nums)
        ones = nums.count(1)
        if ones > 0:
            return n - ones
        
        # the gcd function
        def gcd(n1,n2):
            while n2 and n1:
                n1 = n1%n2
                n1,n2 = n2,n1 
            return max(n2,n1)
        
        # find the minimum length subarray with gcd 1
        min_len = float('inf')
        for i in range(len(nums)):
            g = nums[i]
            for j in range(i+1,n):
                g = gcd(g,nums[j])
                if g==1:
                    min_len = min(min_len,j-i+1)
                    break
                
        if min_len == float('inf'):
            return -1

        return min_len-1 + (n-1)