entries = []
flag = False
lines = dict()

with open("entry.txt", "r") as file:
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
count = False
def verify(x,y):
    global count
    if not x in lines:
        count = True
        return "dic"
    if not y in lines[x]:
        count = True
        return "lines"
    
general = 0


def run_test(b):  
    global general, count
    temp_list = []
    for tmp in b:
        temp_list.append(int(tmp))
    for e in range(0, len(temp_list)-1):
        x = temp_list[e]
        y = temp_list[e+1]
        if verify(x,y) == "dic":
            # trocar de posição com o próximo 
            temp = temp_list[e]
            temp_list[e] = temp_list[e+1]
            temp_list[e+1] = temp
            run_test(temp_list)
            break
        elif verify(x,y) == "lines":
            # trocar de elemento com o anterior
            temp = temp_list[e]
            temp_list[e] = temp_list[e-1]
            temp_list[e-1] = temp
            run_test(temp_list)
            break
        if count:
            general += temp_list[int(len(b)/2)]
                    
for a in entries:
    b = a.strip().split(",")
    if b != ['']:
        run_test(b)
    print(general)

