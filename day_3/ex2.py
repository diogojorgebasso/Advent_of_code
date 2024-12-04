import re

def calculate_enabled_multiplications(memory):
    # Regex patterns to match different instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    # Initial state
    mul_enabled = True
    total_sum = 0

    # Scan through the memory
    i = 0
    while i < len(memory):
        # Check for mul instruction
        mul_match = mul_pattern.match(memory, i)
        if mul_match:
            if mul_enabled:
                num1, num2 = map(int, mul_match.groups())
                total_sum += num1 * num2
            i += len(mul_match.group(0))
            continue

        # Check for do() instruction
        do_match = do_pattern.match(memory, i)
        if do_match:
            mul_enabled = True
            i += len(do_match.group(0))
            continue

        # Check for don't() instruction
        dont_match = dont_pattern.match(memory, i)
        if dont_match:
            mul_enabled = False
            i += len(dont_match.group(0))
            continue

        # If no match, move to the next character
        i += 1

    return total_sum

# Example input
with open("ex1.txt", "r") as file:
    memory = file.read()
result = calculate_enabled_multiplications(memory)
print("Sum of enabled multiplications:", result)
