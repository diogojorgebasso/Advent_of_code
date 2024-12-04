lInput = []
rInput = []
try:
    with open('entry_ex1.txt', 'r', encoding='utf-8') as file:
        # Read the entire content
        for line in file:
            values = line.split()
            lInput.append(int(values[0]))
            rInput.append(int(values[1]))
except:
    print("error")
    
lInput.sort()
rInput.sort()

distance = 0
for idx, x in enumerate(lInput):
    distance += abs(x - rInput[idx])
print(distance)
