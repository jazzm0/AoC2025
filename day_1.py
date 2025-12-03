current, password = 50, 0

with open('day_1.txt') as ifile:
    for line in ifile:
        if line:
            if line[0] == "R":
                current = (current + int(line[1:])) % 100
            elif line[0] == "L":
                current = (current - int(line[1:])) % 100
            if current == 0:
                password += 1

print(password)
