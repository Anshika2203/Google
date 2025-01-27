from collections import defaultdict
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        DIR = [0, 1, 0, -1, 0]
        m, n, nextColor = len(grid), len(grid[0]), 2
        componentSize = defaultdict(int)

        def paint(r, c, color):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] != 1: return
            grid[r][c] = color
            componentSize[color] += 1
            for i in range(4):
                paint(r + DIR[i], c + DIR[i + 1], color)

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 1: continue  # Only paint when it's an island cell
                paint(r, c, nextColor)
                nextColor += 1

        ans = max(componentSize.values() or [0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0: continue
                neiColors = set()
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i + 1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == 0: continue
                    neiColors.add(grid[nr][nc])
                sizeFormed = 1  # Start with 1, which is matrix[r][c] when turning from 0 into 1
                for color in neiColors:
                    sizeFormed += componentSize[color]
                ans = max(ans, sizeFormed)

        return ans