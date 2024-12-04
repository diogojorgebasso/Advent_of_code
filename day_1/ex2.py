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

total = 0
for x in lInput:
    frequency = rInput.count(x)
    total += x*frequency
    
print(total)
