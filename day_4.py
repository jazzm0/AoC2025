grid = []


def count_rolls(grid):
    count_accessible = 0
    accessible_rolls = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                adjacent_rolls = 0
                if i > 0 and grid[i - 1][j] == "@":  # up
                    adjacent_rolls += 1
                if i > 0 and j > 0 and grid[i - 1][j - 1] == "@":  # left up
                    adjacent_rolls += 1
                if i > 0 and j < len(grid[i]) - 1 and grid[i - 1][j + 1] == "@":  # right up
                    adjacent_rolls += 1
                if i < len(grid) - 1 and grid[i + 1][j] == "@":  # down
                    adjacent_rolls += 1
                if i < len(grid) - 1 and j < len(grid) - 1 and grid[i + 1][j + 1] == "@":  # right down
                    adjacent_rolls += 1
                if i < len(grid) - 1 and j > 0 and grid[i + 1][j - 1] == "@":  # left down
                    adjacent_rolls += 1
                if j > 0 and grid[i][j - 1] == "@":  # left
                    adjacent_rolls += 1
                if j < len(grid[i]) - 1 and grid[i][j + 1] == "@":  # right
                    adjacent_rolls += 1
                if adjacent_rolls < 4:
                    count_accessible += 1
                    accessible_rolls.append((i, j))
    return count_accessible, accessible_rolls


with open('day_4.txt') as ifile:
    for line in ifile:
        if line:
            detailed_line = []
            for i in line.strip():
                detailed_line.append(i)
            grid.append(detailed_line)

total = 0

accessible_count, accessible_positions = count_rolls(grid)
print(accessible_count)

while accessible_count > 0:
    total += accessible_count
    for pos in accessible_positions:
        i, j = pos
        grid[i][j] = "."
    accessible_count, accessible_positions = count_rolls(grid)

print(total)
