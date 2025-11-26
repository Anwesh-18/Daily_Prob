from typing import List
def numberOfPaths(grid: List[List[int]], k: int) -> int:
    MOD = 10 ** 9 + 7
    m = len(grid)
    n = len(grid[0])

    dp = [[[0] * k for _ in range(n)] for _ in range(m)]

    dp[0][0][grid[0][0] % k] = 1

    for i in range(m):
        for j in range(n):
            for r in range(k):
                if dp[i][j][r] == 0:
                    continue

                if i + 1 < m:
                    x = (r + grid[i + 1][j]) % k
                    dp[i + 1][j][x] = (dp[i + 1][j][x] + dp[i][j][r]) % MOD

                if j + 1 < n:
                    x = (r + grid[i][j + 1]) % k
                    dp[i][j + 1][x] = (dp[i][j + 1][x] + dp[i][j][r]) % MOD

    return dp[m - 1][n - 1][0]

# Example
print(numberOfPaths([[5,2,4],[3,0,5],[0,7,2]],3))