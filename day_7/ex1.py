# evalute left to right => add parentheses to the expression
from itertools import product

total_sum = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        target, nums = line.split(":")
        target = int(target)
        numbers = list(map(int, nums.split()))
        # identify all possible combinations of operators
        for ops in product("+*", repeat=len(numbers) - 1):
            expr = "("*len(ops) + str(numbers[0])
            for i, op in enumerate(ops):
                expr += op + str(numbers[i + 1]) + ")"
            if eval(expr) == target:
                total_sum += target
                break

print(total_sum)