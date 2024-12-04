import re
with open('ex1.txt', 'r', encoding='utf-8') as file:
    x = re.findall(r'mul\(\d+,\d+\)', file.read())  
    sumnumber = 0
    for x in x:
        x = x.replace('mul(', '')
        x = x.replace(')', '')
        x = x.split(',')
        sumnumber += int(x[0]) * int(x[1])
print(sumnumber)