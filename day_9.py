red_tiles = []

with open('day_9.txt') as f:
    for raw in f:
        r = raw.rstrip('\n')
        coords = r.split(',')
        red_tiles.append((int(coords[1]), int(coords[0])))

red_tiles.sort()

max_tiles = 0
for i in range(0, len(red_tiles)):
    for j in range(0, len(red_tiles)):
        if i != j:
            current_tile = (abs(red_tiles[i][0] - red_tiles[j][0]) + 1) * (abs(red_tiles[i][1] - red_tiles[j][1]) + 1)
            max_tiles = max(current_tile, max_tiles)

print(max_tiles)
