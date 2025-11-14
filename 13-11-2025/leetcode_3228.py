class Solution: 
    def maxOperations(self, s: str) -> int: 
        ops = 0
        ones = 0
        n = len(s)
        for i, ch in enumerate(s):
            if ch == '1':
                ones += 1
            else:
                if i+1 == n or s[i+1] == '1':
                    ops += ones
        return ops