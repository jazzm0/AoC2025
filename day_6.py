numbers = []
operations = []

with open("day_6.txt") as f:
    for line in f:
        s = line.strip()
        if s.find("+") != -1 or s.find("*") != -1:
            parts = s.split(" ")
            for part in parts:
                if part != "":
                    operations.append(part)
        else:
            line = []
            parts = s.split(" ")
            for part in parts:
                if part != "":
                    line.append(int(part))
            numbers.append(line)

result = 0
for j in range(len(numbers[0])):
    sub_result = 0
    operation = operations[j]
    if operation == "*":
        sub_result = 1
    for i in range(len(numbers)):
        if operation == "+":
            sub_result += numbers[i][j]
        elif operation == "*":
            sub_result *= numbers[i][j]
    result += sub_result

print(result)
