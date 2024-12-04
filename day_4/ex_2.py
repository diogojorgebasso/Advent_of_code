with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file if line.strip()]
rows, cols = len(grid), len(grid[0])
word = "MAS"
count = 0
for r in range(1, rows-1):
    for c in range(1, cols-1):
        if grid[r][c] == "A":
            if grid[r-1][c-1] != grid[r+1][c+1] and grid[r-1][c+1] != grid[r+1][c-1]:
                adjecents = [grid[r-1][c-1], grid[r+1][c+1], grid[r-1][c+1], grid[r+1][c-1]]
                print(adjecents)
                if adjecents.count("M") == 2 and adjecents.count("S") == 2:
                    count +=1
print(count)