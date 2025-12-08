def max_joltage(bank):
    mj = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            mj = max(mj, int(bank[i] + bank[j]))
    return mj


solution = 0

with open('day_3.txt') as ifile:
    for line in ifile:
        if line:
            bank = line.strip()
            joltage = max_joltage(bank)
            solution += joltage

print(solution)
