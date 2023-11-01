FILE_NAME = 'starting_numbers.txt'
NB_TURNS_PART1 = 2020
NB_TURNS_PART2 = 30000000

# PART 1
def get_last_spoken_number_part1(file):
    start_numbers = file.readline().split(',')

    elapsed_turns = {}
    current_turn = 1
    last_nb_said = -1

    for i in range(NB_TURNS_PART1):
        if current_turn <= len(start_numbers):
            elapsed_turns[start_numbers[i]] = [current_turn]
            last_nb_said = start_numbers[i]
        else:
            if len(elapsed_turns[last_nb_said]) < 2:
                if "0" in elapsed_turns.keys():
                    elapsed_turns["0"] = elapsed_turns["0"] + [current_turn]
                else:
                    elapsed_turns["0"] = [current_turn]
                last_nb_said = "0"
            else:
                last_nb_said = str(elapsed_turns[last_nb_said][-1] - elapsed_turns[last_nb_said][-2])
                if last_nb_said in elapsed_turns.keys():
                    elapsed_turns[last_nb_said] = elapsed_turns[last_nb_said] + [current_turn]
                else:
                    elapsed_turns[last_nb_said] = [current_turn]
        current_turn += 1
    return last_nb_said

def rambunctious_recitation_part1():
    file = open(FILE_NAME, "r")
    last_nb = get_last_spoken_number_part1(file)
    file.close()
    return last_nb

# PART 2
def get_last_spoken_number_part2(file):
    start_numbers = file.readline().split(',')
    start_numbers = [int(nb) for nb in start_numbers]
    last_index = {}
    for i,n in enumerate(start_numbers):
        if i != len(start_numbers)-1:
            last_index[n] = i

    while len(start_numbers) < NB_TURNS_PART2:
        prev = start_numbers[-1]
        prev_prev = last_index.get(prev, -1)
        last_index[prev] = len(start_numbers)-1
        if prev_prev == -1:
            next_ = 0
        else:
            next_ = len(start_numbers) - 1 - prev_prev
        start_numbers.append(next_)
    return start_numbers[-1]

def rambunctious_recitation_part2():
    file = open(FILE_NAME, "r")
    last_nb = get_last_spoken_number_part2(file)
    file.close()
    return last_nb

### TEST AREA
# Part 1
# print(rambunctious_recitation_part1())
# Output: 447

# Part 2
# print(rambunctious_recitation_part2())
# Output: 11721679
