FILE_NAME = "xmas.txt"

# PART 1
def check_encoding_error(array, sum_to_find):
    for nb in array:
        if nb < sum_to_find and sum_to_find - nb in array:
            return None
    return sum_to_find

def find_encoding_error_part1(file):
    array = list()
    window_size = 25
    index = 0

    for line in file:
        if index < window_size:
            array.append(int(line))
            index += 1
        else:
            sum_to_find = int(line)
            encoding_error = check_encoding_error(array, sum_to_find)
            if encoding_error == None:
                array.pop(0)
                array.append(int(line))
            else:
                return encoding_error
    return -1

def encoding_error_part1():
    file = open(FILE_NAME, "r")
    encoding_error_number = find_encoding_error_part1(file)
    file.close()
    return encoding_error_number

# PART 2
def find_encoding_error_part2(file):
    ref_number = encoding_error_part1()
    combinations_array = []
    sum_array = []

    for line in file:
        number = int(line)
        combinations_array = [combinations_array[i]+ [number] for i in range(len(combinations_array)) if sum_array[i] < ref_number]
        sum_array = [sum_array[i] + number for i in range(len(sum_array)) if sum_array[i] < ref_number]

        if ref_number in sum_array:
            break
        else:
            combinations_array.append([number])
            sum_array.append(number)
    index_combination = sum_array.index(ref_number)
    combination = combinations_array[index_combination]
    combination.sort()
    return combination[0] + combination[-1]

def encoding_error_part2():
    file = open(FILE_NAME, "r")
    sum_errors_min_max = find_encoding_error_part2(file)
    file.close()
    return sum_errors_min_max

### TEST AREA
# PART 1
#print(encoding_error_part1())
# OUTPUT: 731031916

# PART 2
#print(encoding_error_part2())
# OUTPUT: 93396727
