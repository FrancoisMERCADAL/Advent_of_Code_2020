FILE_NAME = "adapters.txt"

# PART 1
def determine_count_diffs_product_pt1(file):
    
    jolt = 0
    count_diff_1 = 0
    count_diff_3 = 0

    for line in file:
        array.append(int(line))
    
    while len(array) > 0:
        if jolt + 1 in array:
            array.pop(array.index(jolt + 1))
            jolt += 1
            count_diff_1 += 1
        elif jolt + 3 in array:
            array.pop(array.index(jolt + 3))
            jolt += 3
            count_diff_3 += 1
    return count_diff_1 * (count_diff_3 + 1)

def adapter_array_part1():
    file = open(FILE_NAME, "r")
    product = determine_count_diffs_product_pt1(file)
    file.close()
    return product

# PART 2
array = []
file = open(FILE_NAME, "r")
for line in file:
    array.append(int(line))
file.close()

nb_ways = 1

array.sort()
print(array)

for val in array:
    if val + 2 in array:
        nb_ways += 3 * nb_ways
    elif val + 1 in array:
        nb_ways += 2 * nb_ways
    else:
        continue

print(nb_ways)



### TEST AREA
# PART 1
#print(adapter_array_part1())
# OUTPUT: 1998

# PART 2
#print()
# OUTPUT: 