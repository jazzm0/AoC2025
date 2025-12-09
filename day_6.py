numbers = []
operations = []
cephalopod = []

with open("day_6.txt") as f:
    for raw in f:
        s = raw.rstrip('\n')
        if s.find("+") != -1 or s.find("*") != -1:
            parts = s.split(" ")
            for part in parts:
                if part != "":
                    operations.append(part)
        else:
            raw = []
            cephalopod.append(s)
            parts = s.split(" ")
            for part in parts:
                if part != "":
                    raw.append(int(part))
            numbers.append(raw)

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

result = 0
matrix_size = len(cephalopod[0]) - 1
len_operations = len(operations) - 1
sub_result = 0
for j in range(matrix_size, -1, -1):
    operation = operations[len_operations]

    current_number = ""
    block_finished = False
    i = 0
    while not block_finished:
        while i < len(cephalopod):
            if cephalopod[i][j] == " ":
                i += 1
                break
            else:
                current_number += cephalopod[i][j]
                i += 1

        if current_number != "":
            current_number_int = int(current_number)
            if operation == "+":
                sub_result += current_number_int
            elif operation == "*":
                if sub_result == 0:
                    sub_result = 1
                sub_result *= current_number_int

            block_finished = True

        elif i == len(cephalopod):
            result += sub_result
            sub_result = 0
            len_operations -= 1

            block_finished = True

print(result + sub_result)
