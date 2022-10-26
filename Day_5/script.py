FILE_NAME = 'seats.txt'

def calculate_id(row_str, column_str, row_interval, column_interval):
    ### ROW Select
    for i in range(len(row_str)):
        if i == len(row_str) - 1:
            if row_str[i] == 'F':
                selected_row = row_interval[0]
            else:
                selected_row = row_interval[1]
        else:
            if row_str[i] == 'F':
                row_interval = [row_interval[0], int((row_interval[1] + row_interval[0])/2)]
            else:
                row_interval = [int(((row_interval[1] + row_interval[0])/2) + 1), row_interval[1]]

    ### COLUMN Select
    for i in range(len(column_str)):
        if i == len(column_str) - 1:
            if column_str[i] == 'R':
                selected_column = column_interval[1]
            else:
                selected_column = column_interval[0]
        else:
            if column_str[i] == 'R':
                column_interval = [int((column_interval[1] + column_interval[0])/2) + 1,column_interval[1]]
            else:
                column_interval = [column_interval[0], int((column_interval[1] + column_interval[0])/2)]
    id = 8 * selected_row + selected_column
    return id

# PART 1
def get_max_seat_id(file):
    ID_array = []
    for line in file:
        row_str = line[0:7]
        column_str = line[7:]
        row_interval = [0,127]
        column_interval = [0,7]
        id = calculate_id(row_str, column_str, row_interval, column_interval)
        ID_array.append(id)
    return max(ID_array)

def binary_coding_part_1():
    file = open(FILE_NAME, "r")
    max_id = get_max_seat_id(file)
    file.close()
    return max_id

# PART 2
def get_missing_seat_id(file):
    ID_array = []
    for line in file:
        row_str = line[0:7]
        column_str = line[7:]
        row_interval = [0,127]
        column_interval = [0,7]
        id = calculate_id(row_str, column_str, row_interval, column_interval)
        ID_array.append(id)
    ID_array.sort()
    for i in range(len(ID_array)-1):
        if ID_array[i+1] == ID_array[i] + 2:
            id_seat = ID_array[i] + 1
            break
    return id_seat

def binary_coding_part_2():
    file = open(FILE_NAME, "r")
    id = get_missing_seat_id(file)
    file.close()
    return id


### TEST AREA

# PART 1
print(binary_coding_part_1())
## OUTPUT: 880

# PART 2
print(binary_coding_part_2())
##OUTPUT: 731