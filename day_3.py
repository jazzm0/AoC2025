def max_joltage(bank):
    k = 12
    stack = []
    to_remove = len(bank) - k
    for digit in bank:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    return int(''.join(stack[:k]))


solution = 0

with open('day_3_small.txt') as ifile:
    for line in ifile:
        if line:
            bank = line.strip()
            joltage = max_joltage(bank)
            solution += joltage

print(solution)
