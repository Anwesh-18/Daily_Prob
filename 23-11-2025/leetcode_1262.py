from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            temp = dp[:]
            for i in range(3):
                new_sum = temp[i] + num
                dp[new_sum % 3] = max(dp[new_sum % 3], new_sum)
        
        return dp[0]