with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file if line.strip()]
rows, cols = len(grid), len(grid[0])
directions = [
    (0, 1),   # Right
    (1, 0),   # Down
    (1, 1),   # Diagonal Down-Right
    (1, -1),  # Diagonal Down-Left
    (0, -1),  # Left
    (-1, 0),  # Up
    (-1, -1), # Diagonal Up-Left
    (-1, 1)   # Diagonal Up-Right
]
    
def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols

word = "XMAS"
def check_direction(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

count = 0
for x in range(rows):
    for y in range(cols):
        for dx, dy in directions:
            if check_direction(x, y, dx, dy):
                count += 1
print(count)


