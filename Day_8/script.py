FILE_NAME = 'commands.txt'

def open_input_file(file):
    array = []
    for line in file:
        line = line.split(' ')
        command = line[0]
        value = int(line[1])
        array.append([command, value])
    return array

# PART 1
def determine_accumulator_part1(file):  
    array = open_input_file(file)
    index_visited = []
    accumulator = 0

    index = 0
    while index not in index_visited:
        index_visited.append(index)
        command = array[index][0]
        value = array[index][1]

        if command == 'acc':
            accumulator += value
            index+= 1
        elif command == 'nop':
            index += 1
        else:
            index += value
    return accumulator

def handheld_halting_part1():
    file = open(FILE_NAME, "r")
    accumulator = determine_accumulator_part1(file)
    file.close()
    return accumulator

# PART 2
file = open(FILE_NAME, "r")
array = open_input_file(file)
print(array)
file.close()

### TEST AREA
# PART 1
#print(handheld_halting_part1())
# OUTPUT: 2003

# PART 2

# OUTPUT: 