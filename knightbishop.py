# n*n chess board
# there is 1 knight and 1 bishop on the board
# input will be knight's startRow, startCol, bishop's startRow, bishop's startCol
# also input will have knight's endRow, endCol.
# knight has to reach to end square without getting killed by bishop (bishop is static and could not move) that means don't move to a sqaure where bishop can kill from bishop given start position.
# Also knight can kill bishop that means after that it can move to any direction.
# output will be the minimum number of moves required to reach end position from start position of knight.
# if it is not possible to reach end position then output will be -1.

# (+2, +1), (+2, -1), (-2, +1), (-2, -1),
# (+1, +2), (+1, -2), (-1, +2), (-1, -2)
# bfs

from collections import deque
from typing import Tuple

def minKnightMoves(n: int, knightStart: Tuple[int, int], knightEnd:Tuple[int, int], bishopStart: Tuple[int, int]) -> int:
    knightMoves = [
        (+2, +1), (+2, -1), (-2, +1), (-2, -1),
        (+1, +2), (+1, -2), (-1, +2), (-1, -2)
    ]

    bishopRow, bishopCol = bishopStart
    
    def under_attack(row, col):
        return abs(row-bishopRow) == abs(col-bishopCol)
    
    queue=deque([(knightStart[0], knightEnd[0], 0, False)])
    visited=set([(knightStart[0], knightEnd[0], False)])

    while queue:
        row, col, moves, bishopCaptured = queue.popleft()

        if (row, col) == knightEnd:
            return moves
        
        for dr, dc in knightMoves:
            newRow, newCol = dr+row, dc+col

            if 0 <= newRow <n and 0 <= newCol <n:
                if bishopCaptured or not under_attack(newRow, newCol):
                    newState = newRow, newCol, bishopCaptured or (newRow == bishopRow and newCol == bishopCol)
                    if newState not in visited:
                        visited.add(newState)
                        queue.append((newRow, newCol, moves+1, bishopCaptured or (newRow == bishopRow and newCol == bishopCol)))
    return -1


n = 8
knightStart = (0, 0)
bishopStart = (4,3)
knightEnd = (7, 7)

print(minKnightMoves(n, knightStart, bishopStart, knightEnd))