def topological_sort(nodes, edges):
    in_degree = {n:0 for n in nodes}
    for u in edges:
        for v in edges[u]:
            in_degree[v] += 1

    queue = [n for n in nodes if in_degree[n] == 0]
    result = []
    while queue:
        u = queue.pop()
        result.append(u)
        if u in edges:
            for v in edges[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
    return result


rules = {}
updates = []
with open("input.txt", "r") as f:
    # Ler regras
    for line in f:
        line = line.strip()
        if line == "":
            # Linha em branco encontrada, parar de ler regras
            break
        a, b = line.split("|")
        a, b = int(a), int(b)
        if a not in rules:
            rules[a] = []
        rules[a].append(b)
    for line in f:
        line=line.strip()
        if line:
            update = list(map(int, line.split(",")))
            updates.append(update)

def is_correctly_ordered(update, rules):
    pos = {p: i for i,p in enumerate(update)}
    for x in rules:
        for y in rules[x]:
            if x in pos and y in pos:
                if pos[x] > pos[y]:
                    return False
    return True

def reorder_update(update, rules):
    pages = set(update)
    subgraph = {}
    for x in rules:
        for y in rules[x]:
            if x in pages and y in pages:
                if x not in subgraph:
                    subgraph[x] = []
                subgraph[x].append(y)

    sorted_pages = topological_sort(pages, subgraph)
    return sorted_pages

def middle_page(update):
    # update tem tamanho ímpar
    return update[len(update)//2]

sum_correct = 0
sum_incorrect = 0

incorrect_updates = []
for upd in updates:
    if is_correctly_ordered(upd, rules):
        sum_correct += middle_page(upd)
    else:
        incorrect_updates.append(upd)

# Agora arrumar os incorretos
for upd in incorrect_updates:
    corrected = reorder_update(upd, rules)
    sum_incorrect += middle_page(corrected)

print("Soma das páginas do meio dos updates já corretos (Parte 1):", sum_correct)
print("Soma das páginas do meio dos updates após correção (Parte 2):", sum_incorrect)
