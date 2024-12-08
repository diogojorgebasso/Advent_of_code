grafo_dirigido = {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13]}
candidatos = [75,97,47,61,53]

def swap(x, y):
    idx_x = candidatos.index(x)
    idx_y = candidatos.index(y)
    candidatos[idx_x], candidatos[idx_y] = candidatos[idx_y], candidatos[idx_x]
for _ in candidatos:
    for c in candidatos:
        # changer pour la premiere 
        possible = True
        for d in candidatos:
            if d in grafo_dirigido and c in grafo_dirigido[d]:
                possible = False
    if possible:
        print(candidatos)
        swap(d,c)

print(candidatos)