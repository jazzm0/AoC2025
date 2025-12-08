solution = 0

with open('day_2.txt') as ifile:
    for line in ifile:
        if line:
            for r in line.strip().split(","):
                ranges = r.split("-")
                low, high = int(ranges[0]), int(ranges[1])
                for id in range(low, high + 1):
                    string_id = str(id)
                    length = len(string_id)
                    if length % 2 == 0 and string_id[:length // 2] == string_id[length // 2:]:
                        solution += id

print(solution)
