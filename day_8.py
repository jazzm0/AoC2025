from math import sqrt

unconnected_boxes = []

with open('day_8.txt') as f:
    for raw in f:
        r = raw.rstrip('\n')
        coords = r.split(',')
        unconnected_boxes.append((int(coords[0]), int(coords[1]), int(coords[2])))


def distance(box1, box2):
    return sqrt((box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2)


distances = dict()
for i in range(len(unconnected_boxes)):
    for j in range(i + 1, len(unconnected_boxes)):
        box1 = unconnected_boxes[i]
        box2 = unconnected_boxes[j]
        dist = distance(box1, box2)
        same_distance = distances.get(dist, [])
        same_distance.append((box1, box2))
        distances[dist] = same_distance

# Sort all pairs by distance
sorted_distances = sorted(distances.keys())
sorted_pairs = []
for d in sorted_distances:
    sorted_pairs.extend(distances[d])

already_connected = []


def find_circuit_index(box):
    for idx, circuit in enumerate(already_connected):
        if box in circuit:
            return idx
    return None


# Connect the first 1000 closest pairs
connections_to_make = 1000
for k in range(connections_to_make):
    box1, box2 = sorted_pairs[k]
    i1 = find_circuit_index(box1)
    i2 = find_circuit_index(box2)

    if i1 is None and i2 is None:
        new_circuit = set()
        new_circuit.add(box1)
        new_circuit.add(box2)
        already_connected.append(new_circuit)
    elif i1 is not None and i2 is None:
        already_connected[i1].add(box2)
    elif i1 is None and i2 is not None:
        already_connected[i2].add(box1)
    else:
        if i1 != i2:
            already_connected[i1].update(already_connected[i2])
            already_connected.pop(i2)

lengths = [len(c) for c in already_connected]
lengths.sort(reverse=True)

print(lengths[0] * lengths[1] * lengths[2])
