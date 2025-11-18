from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        left = 0

        while left<len(bits):
            if bits[left] == 0:
                left+=1
            else:
                left += 2
        
        return left == len(bits)-1