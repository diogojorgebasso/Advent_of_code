# evalute left to right => add parentheses to the expression
from itertools import product

total_sum = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        target, nums = line.split(":")
        target = int(target)
        numbers = list(map(int, nums.split()))
        for ops in product("+*|", repeat=len(numbers) - 1):
            expr = str(numbers[0])
            temp_result = numbers[0]
            for i, op in enumerate(ops):
                if op == "|":
                    temp_result = int(str(temp_result) + str(numbers[i + 1]))
                elif op == "+":
                    temp_result += numbers[i + 1]
                else:
                    temp_result *= numbers[i + 1]
            if temp_result  == target:
                total_sum += target
                break

print(total_sum)