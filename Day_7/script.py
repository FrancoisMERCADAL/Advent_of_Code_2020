FILE_NAME = "luggage_rules.txt"

### PART 1
def open_parse_file():
    rules_dict = {}
    file = open(FILE_NAME, "r")
    while True:
        line = file.readline()
        if not line:
            break
        line = line.split(" bags contain ")
        color = line[0]
        rules = line[1].split(", ")
        rules[-1] = rules[-1][:-2]
        for i in range(len(rules)):
            rules[i] = rules[i].split()[1:]
            rules[i] = [word for word in rules[i] if word not in ["bag", "bags"]]
            rules[i] = ' '.join(rules[i])
        rules_dict[color] = rules
    file.close()
    return rules_dict

def count_bags(rules_dict, colors_list, counted_colors, count):
    if len(colors_list) > 0:
        colors_list_new = []
        for color in colors_list:
            for key, value in rules_dict.items():
                if color in value and key not in counted_colors:
                    count += 1
                    colors_list_new.append(key)
                    counted_colors.append(key)
        return count_bags(rules_dict, colors_list_new, counted_colors, count)
    else:
        return count

def luggage_part1():
    rules_dict = open_parse_file()
    goal_color = ["shiny gold"]
    count = 0
    return count_bags(rules_dict, goal_color, goal_color, count)
    
### PART 2
def open_parse_file_part2():
    file = open(FILE_NAME, "r")
    rules_dict = {}
    while True:
        line = file.readline()
        if not line:
            break
        line = line.split(" bags contain ")
        color = line[0]
        rules = line[1].split(", ")
        rules[-1] = rules[-1][:-2]
        for i in range(len(rules)):
            rules[i] = rules[i].split()
            rules[i] = [word for word in rules[i] if word not in ["bag", "bags"]]
            rules[i] = [rules[i][0], ' '.join(rules[i][1:])]
            if rules[i] == ['no', 'other']:
                rules = None
        rules_dict[color] = rules
    file.close()
    return rules_dict

goal_color = "shiny gold"
rules_dict = open_parse_file_part2()
print(rules_dict)
count = 0

def count_bags_part2(rules_dict, color_target, multiplicator, count):
    print("#######")
    print(color_target)
    if color_target != None:        
        list_luggage = rules_dict[color_target]
        print(count, multiplicator)
        print(list_luggage)
        for luggage in list_luggage:
            print(luggage)
            if rules_dict[luggage[1]] == None:
                count += multiplicator * int(luggage[0])
            else:
                new_count = count + multiplicator * int(luggage[0])
                multiplicator *= int(luggage[0])
                count = count_bags_part2(rules_dict, luggage[1], multiplicator, new_count)
        return count

print(count_bags_part2(rules_dict, goal_color, 1, 0))

### TEST AREA
## PART 1
#print(luggage_part1())
## OUTPUT: 226

## PART 2

## OUTPUT
