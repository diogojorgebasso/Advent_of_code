entries = []
flag = False
lines = dict()

with open("input.txt", "r") as file:
    for line in file:
        if line == "\n":
            flag = True
        if flag:
            entries.append(line)
        else:
            a,b = line.split("|")
            a = int(a)
            b = int(b)
            if a not in lines:
                lines[a] = []
            lines[a].append(b)

def verify(x,y):
    if x in lines:
        if y in lines[x]:
            return True
    return False

general = 0
for a in entries:
    b = a.strip().split(",")
    if b != ['']:
        count = 0
        print(b)
        print(lines)
        for e in range(0, len(b)-1):
            x = int(b[e])
            y = int(b[e+1])
            print(x,y)
            if verify(x,y):
                count += 1
                if count == len(b)-1:
                    general += int(b[int(len(b)/2)])
                    print(general)
            else:
                break
print(general)

