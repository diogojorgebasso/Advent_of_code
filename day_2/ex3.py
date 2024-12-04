total_reports = 0
with open('ex2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        unsafe = False
        reports = line.split()
        for idx, r in enumerate(reports):
            reports[idx] = int(r)
        ascending = False
        first = reports[0]
        if reports[1] > reports[0]:
            ascending = True
        for r in range(1, len(reports)):
            if abs(reports[r] - first) < 4 and abs(reports[r] - first) > 0:
                if reports[r] > first and ascending:
                    first = reports[r]
                elif reports[r] < first and not ascending:
                    first = reports[r]
                else:
                    unsafe = True
            else:
                unsafe = True
                
        if not unsafe:
            total_reports+=1
print(total_reports)
