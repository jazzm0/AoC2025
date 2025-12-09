tachyon_manifold = []

with open("day_7.txt") as f:
    for raw in f:
        row = []
        s = raw.rstrip('\n')
        for c in s:
            row.append(c)
        tachyon_manifold.append(row)

split_count = 0
for i in range(len(tachyon_manifold)):
    for j in range(len(tachyon_manifold[0])):
        if tachyon_manifold[i][j] == "S":
            tachyon_manifold[i + 1][j] = "|"
            break
        elif tachyon_manifold[i][j] == "|" and i < len(tachyon_manifold) - 1:
            if tachyon_manifold[i + 1][j] == "^":
                tachyon_manifold[i + 1][j - 1] = "|"
                tachyon_manifold[i + 1][j + 1] = "|"
                split_count += 1
            else:
                tachyon_manifold[i + 1][j] = "|"
print(split_count)
