import heapq

rows,cols = map(int,input().split())
matrix = []
matrix = [list(map(int, input().split())) for _ in range(rows)]
effort_to = [[float('inf')] * cols for _ in range(rows)]
effort_to[0][0] = 0
# Directions(up,down,right,left)
directions = [(-1,0), (1,0), (0,1), (0,-1)]

# starting point
effort,i,j=0,0,0
heap = []
heapq.heappush(heap,(effort,i,j))

while heap:
    effort,r,c = heapq.heappop(heap)
    
    for dr,dc in directions:
        nr = r + dr
        nc = c + dc
        if 0<= nr < rows and 0<= nc < cols:
            diff = abs(matrix[nr][nc] - matrix[r][c])
            new_effort = max(effort,diff)
            if new_effort < effort_to[nr][nc]:
                effort_to[nr][nc] = new_effort
                heapq.heappush(heap,(new_effort,nr,nc))
print(effort_to[rows-1][cols-1])