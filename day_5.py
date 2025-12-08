import bisect


def merge_ranges(ranges):
    if not ranges:
        return []

    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end or (start == last_end + 1):
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged



ranges = []
ingredients = []
with open("day_5.txt") as f:
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
ranges = merge_ranges(ranges)
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
total_fresh = 0
for idx in range(len(ranges)):
    total_fresh += ranges[idx][1] - ranges[idx][0] + 1
print(total_fresh)

