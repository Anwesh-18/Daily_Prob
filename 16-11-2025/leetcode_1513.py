def numSub(s: str) -> int:
        MOD = 10**9 + 7
        s += "0"
        count = 0
        left = 0
        for right in range(len(s)):
            if s[right] == '0':
                n = right - left
                if n > 0:
                    count += n * (n + 1) // 2
                left = right + 1
        
        return count % MOD

print(numSub("0110111"))