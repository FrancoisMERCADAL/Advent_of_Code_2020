FILE_NAME = "seats.txt"

# PART 1
def assert_values(lines, row, column):
    try:
        if lines[row][column] == "#" and row >= 0 and column >= 0:
            return 1
        return 0
    except:
        return 0

def get_nb_neighbours(lines, row, column):
    array = [
        assert_values(lines, row, column-1),
        assert_values(lines, row-1, column-1),
        assert_values(lines, row-1, column),
        assert_values(lines, row-1, column+1),
        assert_values(lines, row, column+1),
        assert_values(lines, row+1, column+1),
        assert_values(lines, row+1, column),
        assert_values(lines, row+1, column-1),
    ]
    return sum(array)

def count_occupied_seats(file):
    lines = []
    occupied_seats = 0

    # open file + 1st round
    for line in file:
            lines.append(list(line.replace("L", "#")))
            occupied_seats += list(line.replace("L", "#")).count("#")

    ## next rounds
    nb_changes = None

    while True:
        nb_changes = 0
        seats_to_free = []
        seats_to_occupy = []
        for i in range(len(lines)):
            for k in range(len(lines[i])):
                if lines[i][k] != ".":
                    neighbours = get_nb_neighbours(lines, i, k)
                    if neighbours == 0 and lines[i][k] == "L":
                        seats_to_occupy.append((i,k))
                        nb_changes += 1
                    elif neighbours >= 4 and lines[i][k] == "#":
                        seats_to_free.append((i,k))
                        nb_changes += 1

        if nb_changes == 0:
            break
        for t in seats_to_free:
            lines[t[0]][t[1]] = "L"
            occupied_seats -= 1
        for t in seats_to_occupy:
            lines[t[0]][t[1]] = "#"
            occupied_seats += 1

    return occupied_seats

def seating_system_part1():
    file = open(FILE_NAME, "r")
    occupied_seats = count_occupied_seats(file)
    file.close()
    return occupied_seats

# PART 2
def assert_values_v2(lines, row, column, coef_x, coef_y):
    try:
        while True:
            row += coef_x
            column += coef_y
            if lines[row][column] == "#" and row >= 0 and column >= 0:
                return 1
            elif lines[row][column] == "L" and row >= 0 and column >= 0:
                return 0
    except:    
        return 0

def get_nb_neighbours_v2(lines, row, column):
    array = [
        assert_values_v2(lines, row, column, 0, -1),
        assert_values_v2(lines, row, column, -1, -1),
        assert_values_v2(lines, row, column, -1, 0),
        assert_values_v2(lines, row, column, -1, 1),
        assert_values_v2(lines, row, column, 0, 1),
        assert_values_v2(lines, row, column, 1, 1),
        assert_values_v2(lines, row, column, 1, 0),
        assert_values_v2(lines, row, column, 1, -1)
    ]
    return sum(array)

def count_occupied_seats_v2(file):
    lines = []
    occupied_seats = 0

    # open file + 1st round
    for line in file:
        lines.append(list(line.replace("L", "#")))
        occupied_seats += list(line.replace("L", "#")).count("#")

    ## next rounds
    nb_changes = None

    while True:
        nb_changes = 0
        seats_to_free = []
        seats_to_occupy = []
        for i in range(len(lines)):
            for k in range(len(lines[i])):
                if lines[i][k] != ".":
                    neighbours = get_nb_neighbours_v2(lines, i, k)
                    if neighbours == 0 and lines[i][k] == "L":
                        seats_to_occupy.append((i,k))
                        nb_changes += 1
                    elif neighbours >= 5 and lines[i][k] == "#":
                        seats_to_free.append((i,k))
                        nb_changes += 1

        if nb_changes == 0:
                break
        for t in seats_to_free:
            lines[t[0]][t[1]] = "L"
            occupied_seats -= 1
        for t in seats_to_occupy:
            lines[t[0]][t[1]] = "#"
            occupied_seats += 1

    return occupied_seats

def seating_system_part2():
    file = open(FILE_NAME, "r")
    occupied_seats = count_occupied_seats_v2(file)
    file.close()
    return occupied_seats

### TEST AREA
# PART 1
#print(seating_system_part1())
# OUTPUT: 2289

# PART 2
#print(seating_system_part2())
# OUTPUT: 2059
