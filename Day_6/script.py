FILE_NAME = 'questions_answers.txt'

### PART 1
def get_sum_answers_1(file):
    string = ''
    array = []
    for line in file:
        if line in ['\n', ' ']:
            array.append(len(set(string)))
            string = ''
        else:
            string += line[:-1]
    return sum(array)

def custom_customs_part_1():
    file = open(FILE_NAME, "r")
    sum = get_sum_answers_1(file)
    file.close()
    return sum

### PART 2
def get_sum_answers_2(file):
    dictionary = {}
    array = []
    count = 0
    nb_people = 0
    for line in file:
        if line in ['\n', ' ']:
            for key in dictionary.keys():
                if dictionary[key] == nb_people:
                    count += 1
            array.append(count)
            count = 0
            nb_people = 0
            dictionary = {}
        else:
            nb_people += 1
            for char in line[:-1]:
                if char in dictionary:
                    dictionary[char] += 1
                else:
                    dictionary[char] = 1
    return sum(array)

def custom_customs_part_2():
    file = open(FILE_NAME, "r")
    sum = get_sum_answers_2(file)
    file.close()
    return sum

### TEST AREA
## PART 1
print(custom_customs_part_1())
## OUTPUT: 6735

## PART 2
print(custom_customs_part_2())
## OUTPUT: 3221