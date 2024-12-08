with open("entry2.txt", "r") as file:
    grid = [list(line.strip()) for line in file if line.strip()]
rows, cols = len(grid), len(grid[0])

position = [(-1,0), #subir
            (0,1),  #direita
            (1,0),  #descer
            (0,-1)  #esquerda
            ]

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            for pos in position:
                print(pos)
                print(grid[r + pos[0]][c + pos[1]])