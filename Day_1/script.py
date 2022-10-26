FILE_NAME = 'entries.txt'
YEAR = 2020

# PART 1
def calculation_method1(file):
    array = []
    for line in file:
        number = int(line)
        complement = YEAR - number
        if complement in array:
            product = number * complement
            break
        array.append(number)
    return product

def report_repair_part1():
    file = open(FILE_NAME, "r")
    product = calculation_method1(file)
    return product

# PART 2
def calculation_method2(file):
    array = []
    combinations_of_two = []
    for line in file:
        array.append(int(line))
    for i in range(len(array)):
        for k in range(len(array)):
            if i != k:
                combinations_of_two.append([array[i],array[k]])
    for combination in combinations_of_two:
        complement = YEAR - combination[0] - combination[1]
        if complement in array:
            product = complement * combination[0] * combination[1]
            break
    return product

def report_repair_part2():
    file = open(FILE_NAME, "r")
    product = calculation_method2(file)
    return product

# TESTS
## PART 1
print(report_repair_part1())
# OUTPUT: 485739

## PART 2
print(report_repair_part2())
# OUTPUT: 161109702