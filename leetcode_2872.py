from typing import List
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        self.ans = 0
        
        def dfs(node):
            visited[node] = True
            total = values[node]
            
            for nei in graph[node]:
                if not visited[nei]:
                    subtree_sum = dfs(nei)
                    total += subtree_sum
            
            if total % k == 0:
                self.ans += 1
                return 0
            
            return total
        
        dfs(0)
        return self.ans
        