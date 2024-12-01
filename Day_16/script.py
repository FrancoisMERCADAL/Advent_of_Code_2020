FILE_NAME = "tickets.txt"

# PART 1
def get_sum_wrong_numbers(file):
    flag_ticket = False
    flag_nearby_ticket = False
    max_read_val = 0
    min_read_val = 9999
    legal_values = []
    sum_arr = []
    for line in file:
        if line == "your ticket:\n":
            flag_ticket = True
        elif line == "nearby tickets:\n":
            flag_nearby_ticket = True
        elif line == '\n':
            continue
        elif flag_ticket == False and flag_nearby_ticket == False:
            line = line.strip().replace(' ','').split(":")[1].split("or")
            for i in range(len(line)):
                nb_arr = line[i].split('-')
                line[i] = [int(nb_arr[0]),int(nb_arr[1])]
            legal_values += list(range(line[0][0],line[0][1]+1)) + list(range(line[1][0],line[1][1]+1))
            max_read_val = max([max_read_val,line[1][1]])
            min_read_val = min(min_read_val, line[0][0])
        elif flag_ticket == True and flag_nearby_ticket == True:
            line = [int(x) for x in line.strip().split(",")]
            for nb in line:
                if nb < min_read_val or nb > max_read_val or nb not in legal_values:
                    sum_arr.append(nb)
                    break
    return sum(sum_arr)

def ticket_translation_part1():
    file = open(FILE_NAME, "r")
    sum_nb = get_sum_wrong_numbers(file)
    file.close()
    return sum_nb

# PART 2

### TEST AREA
# Part 1
print(ticket_translation_part1())
# Output: 26053
