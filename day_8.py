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

sorted_distances = sorted(distances.keys())
sorted_pairs = []
for d in sorted_distances:
    sorted_pairs.extend(distances[d])

# Initialize each box in its own circuit
already_connected = [{box} for box in unconnected_boxes]


def find_circuit_index(box):
    for idx, circuit in enumerate(already_connected):
        if box in circuit:
            return idx
    return None


connections_to_make = 100000
for k in range(connections_to_make):
    box1, box2 = sorted_pairs[k]
    index_one = find_circuit_index(box1)
    index_2 = find_circuit_index(box2)

    if index_one != index_2:
        # Merge into the circuit with the smaller index
        if index_one > index_2:
            index_one, index_2 = index_2, index_one
        already_connected[index_one].update(already_connected[index_2])
        already_connected.pop(index_2)

        if len(already_connected) == 1:
            print(box1[0] * box2[0])
            break
