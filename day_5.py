import bisect


def count_fresh_ids(path):
    ranges = []
    ingredients = []
    with open(path) as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            if "-" in s:
                a, b = s.split("-")
                ranges.append((int(a), int(b)))
            else:
                ingredients.append(int(s))

    ranges.sort(key=lambda x: x[0])
    lows = [r[0] for r in ranges]
    prefix_max_high = []
    m = -1
    for _, hi in ranges:
        m = max(m, hi)
        prefix_max_high.append(m)

    total = 0
    for x in ingredients:
        idx = bisect.bisect_right(lows, x) - 1
        if idx >= 0 and x <= prefix_max_high[idx]:
            total += 1

    print(total)


if __name__ == "__main__":
    count_fresh_ids('day_5.txt')
