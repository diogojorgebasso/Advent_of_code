caracteres = {}
with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file if line.strip()]
rows, cols = len(grid), len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != ".":
            if grid[r][c] not in caracteres:
                caracteres[grid[r][c]] = []
            caracteres[grid[r][c]].append((c,r))

print(caracteres)

antinodes = set() # tupla de posição de todos os antinodes

def check_antinode(x, y):
    if x < 0 or x >= cols or y < 0 or y >= rows:
        return False
    elif grid[y][x] != ".":
        return False
    return True

for _, value in caracteres.items():
    size_coordinates = len(value)
    for i in range(0, size_coordinates):
        for j in range(i+1, size_coordinates):
            (x_coord1, y_coord1), (x_coord2, y_coord2) = value[i], value[j]
            dx = x_coord2 - x_coord1
            dy = y_coord2 - y_coord1
            count = 1
            while True:
                if x_coord2 + dx * count >= cols or y_coord2 + dy * count >= rows:
                    break
                new_coord_sum = ((x_coord2 + dx * count), (y_coord2 + dy *count))
                print(new_coord_sum)
                if check_antinode(*new_coord_sum):
                    antinodes.add(new_coord_sum)
                count += 1
            count = 1
            while True:
                if x_coord1 - dx * count < 0 or y_coord1 - dy * count < 0:
                    break
                new_coord_diff = ((x_coord1 - dx*count), (y_coord1 - dy*count))
                if check_antinode(*new_coord_diff):
                    antinodes.add(new_coord_diff)
                count += 1
print(antinodes)

def print_final(antinodes):
    for r in range(rows):
        for c in range(cols):
            if (c, r) in antinodes and not grid[r][c] != ".":
                print("#", end="")
            else:
                print(grid[r][c], end="")
        print()

print_final(antinodes)

count = 0
for key, value in caracteres.items():
    if isinstance(value, list) and len(value) != 1:
        count += len(value)


print(len(antinodes) + count)