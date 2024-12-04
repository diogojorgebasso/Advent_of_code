total_reports = 0

def is_safe_report(report):
    ascending = report[1] > report[0]
    first = report[0]

    for r in range(1, len(report)):
        if abs(report[r] - first) < 4 and abs(report[r] - first) > 0:
            if (report[r] > first and ascending) or (report[r] < first and not ascending):
                first = report[r]
            else:
                return False
        else:
                return False
    return True

def dampener():
    total_safe = 0

    with open('ex2.txt', 'r', encoding='utf-8') as file:
        for line in file:
            reports = list(map(int, line.split()))
            if is_safe_report(reports):
                total_safe += 1
            else:
                # Check if removing one level makes the report safe
                for i in range(len(reports)):
                    modified_report = reports[:i] + reports[i+1:]
                    print(modified_report)
                    if is_safe_report(modified_report):
                        total_safe += 1
                        break
    return total_safe

print(dampener())
