import math

FILE_NAME = 'mask_datas.txt'
ENTIRE_ADDRESS_FORMAT = "000000000000000000000000000000000000"

def int_to_bin(nb):
    binary = bin(nb)[2:]
    return list(ENTIRE_ADDRESS_FORMAT[:len(ENTIRE_ADDRESS_FORMAT)-len(binary)] + binary)

def bin_to_int(bin_arr):
    nb = 0
    for i in range(len(bin_arr)):
        if bin_arr[i] == '1':
            nb += math.pow(2, 36 - 1 - i)
    return int(nb)

# PART 1
def get_memory_space_used_part1(file):
    memory_dict = {}
    while file:
        line = file.readline().strip() # strip() removes '\n'
        if line == "":
            break
        line_arr = line.split(" = ")
        if line_arr[0] == 'mask':
            indexes_0 = []
            indexes_1 = []
            for i in range(len(line_arr[1])):
                if line_arr[1][i] == '0':
                    indexes_0.append(i)
                elif line_arr[1][i] == '1':
                    indexes_1.append(i)
        else:
            memory_space = int(line_arr[0].split('[')[1][:-1])
            value = int(line_arr[1])
            value = int_to_bin(value)
            for index in indexes_0:
                value[index] = "0"
            for index in indexes_1:
                value[index] = "1"
            value = bin_to_int(value)
            memory_dict[str(memory_space)] = value
    return sum(memory_dict.values())

def docking_data_part1():
    file = open(FILE_NAME, "r")
    memory = get_memory_space_used_part1(file)
    file.close()
    return memory

# PART 2
def make_combinations(combinations, array, index, nb_X, n_combinations):
    if index == nb_X:
        combinations.append([value for value in array])
    else:
        array[index] = "0"
        make_combinations(combinations, array, index+1, nb_X, n_combinations)
        array[index] = "1"
        make_combinations(combinations, array, index+1, nb_X, n_combinations)
    if len(combinations) == n_combinations:
        return combinations

def get_memory_space_used_part2(file):
    memory_dict = {}
    while file:
        line = file.readline().strip() # strip() removes '\n'
        if line == "":
            break
        line_arr = line.split(" = ")
        if line_arr[0] == 'mask':
            indexes_1 = []
            indexes_X = []
            for i in range(len(line_arr[1])):
                if line_arr[1][i] == '1':
                    indexes_1.append(i)
                elif line_arr[1][i] == 'X':
                    indexes_X.append(i)
            nb_X_combinations = int(math.pow(2, len(indexes_X)))
            X_combinations = make_combinations([], [-1] * len(indexes_X), 0, len(indexes_X), nb_X_combinations)
        else:
            memory_space = int(line_arr[0].split('[')[1][:-1])
            value = int(line_arr[1])
            memory_space = int_to_bin(memory_space)
            if len(indexes_1) > 0:
                for index in indexes_1:
                    memory_space[index] = "1"
            
            if len(indexes_X) > 0:
                for combination in X_combinations:
                    for i in range(len(combination)):
                        memory_space[indexes_X[i]] = combination[i]
                    memory_space_write = bin_to_int(memory_space)
                    memory_dict[str(memory_space_write)] = value
            else:
                memory_space_write = bin_to_int(memory_space)
                memory_dict[str(memory_space_write)] = value
    return sum(memory_dict.values())

def docking_data_part2():
    file = open(FILE_NAME, "r")
    memory = get_memory_space_used_part2(file)
    file.close()
    return memory

### TEST AREA
# Part 1
# print(docking_data_part1())
# Output: 6386593869035

# Part 2
# print(docking_data_part2())
# Output: 4288986482164
