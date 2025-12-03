current, password, x434 = 50, 0, 0

with open('day_1.txt') as ifile:
    for line in ifile:
        if line:
            rotations = int(line[1:])
            x434 += rotations // 100
            rotations %= 100
            if line[0] == "R":
                if current + rotations > 100:
                    x434 += 1
                current = (current + rotations) % 100
            elif line[0] == "L":
                if current != 0 and current - rotations < 0:
                    x434 += 1
                current = (current - rotations) % 100

            if current == 0:
                password += 1

print(password)
print(password + x434)
