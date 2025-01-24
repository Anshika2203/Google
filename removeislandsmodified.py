def remove_islands_no_diagonals(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    # Helper function to perform DFS and mark edge-connected 1s
    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] != 1:
            return
        # Mark the cell as visited by changing it to a special value (e.g., 2)
        matrix[row][col] = 2
        # Visit all 4 cardinal directions (no diagonals)
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
    
    # Step 1: Traverse the edges and mark edge-connected islands
    for r in range(rows):
        for c in [0, cols - 1]:  # Left and right edges
            if matrix[r][c] == 1:
                dfs(r, c)
    for c in range(cols):
        for r in [0, rows - 1]:  # Top and bottom edges
            if matrix[r][c] == 1:
                dfs(r, c)
    
    # Step 2: Remove unconnected islands and restore edge-connected ones
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                matrix[r][c] = 0  # Remove unconnected island
            elif matrix[r][c] == 2:
                matrix[r][c] = 1  # Restore edge-connected island
    
    return matrix

# Example input
matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]

# Removing islands
output = remove_islands_no_diagonals(matrix)

# Print the output
for row in output:
    print(row)

print('ex-2')

# Example input
matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]

# Removing islands
output = remove_islands_no_diagonals(matrix)

# Print the output
for row in output:
    print(row)