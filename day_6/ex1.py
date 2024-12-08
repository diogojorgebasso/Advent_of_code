with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file if line.strip()]
rows, cols = len(grid), len(grid[0])
direction_vector = [(-1,0), #subir
            (0,1),  #direita
            (1,0),  #descer
            (0,-1)  #esquerda
            ]

def is_border(i,j):
    return i == rows-1 or j == cols-1

i,j = 0,0
actual = (-1,0)

def print_grid():
    for line in grid:
        print("".join(line))
    print()

def can_move(i, j, actual):
    temp_x = actual[0]
    temp_y = actual[1]
    if i + temp_x < rows and j + temp_y < cols:
        return grid[i + temp_x][j + temp_y] != "#"

def move(r,c, actual):
    grid[r][c] = "X"
    grid[r + actual[0]][c + actual[1]] = "^"
    
def test():
    global i, j
    global actual
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "^":
                i,j = r,c
                if can_move(r,c, actual):
                    move(r,c, actual)
                    break
                else:                    
                    posicao_atual = direction_vector.index(actual)
                    posicao_futura = (posicao_atual + 1) % 4
                    actual = direction_vector[posicao_futura]
                    break

while True:
    if is_border(i,j):
        break
    else:
        test()

def count_X():
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "X":
                count += 1
    return count

print(count_X()+1)