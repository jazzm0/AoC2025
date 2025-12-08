solution, solution_2 = 0, 0


def is_invalid_1(string_id):
    length = len(string_id)
    if length % 2 == 0 and string_id[:length // 2] == string_id[length // 2:]:
        return True
    return False


def is_invalid_2(string_id):
    length = len(string_id)
    for i in range(1, length):
        if length % i == 0 and string_id[:i] * (length // i) == string_id:
            return True
    return False


with open('day_2.txt') as ifile:
    for line in ifile:
        if line:
            for r in line.strip().split(","):
                ranges = r.split("-")
                low, high = int(ranges[0]), int(ranges[1])
                for id in range(low, high + 1):

                    if is_invalid_1(str(id)):
                        solution += id

                    if is_invalid_2(str(id)):
                        solution_2 += id
print(solution)
print(solution_2)
