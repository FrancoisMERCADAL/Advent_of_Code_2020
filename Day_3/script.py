FILE_NAME = "forest.txt"

def open_file():
    with open(FILE_NAME, "r") as file:
        map_ = list(map(str.strip, file.readlines()))
    return map_

# METHOD 1
slope = {
    "x":3,
    "y": 1
}

def trees_encountered_part1():
    x_position = 0
    trees_encountered = 0
    map_ = open_file()

    for i in range(len(map_)):
        if map_[i][x_position] == "#":
            trees_encountered += 1
        x_position = (x_position + slope["x"]) % len(map_[i])
    return trees_encountered

# METHOD 2
slopes = [
    {
        "x": 1,
        "y": 1
    },
    {
        "x": 3,
        "y": 1
    },
    {
        "x": 5,
        "y": 1
    },
    {
        "x": 7,
        "y": 1
    },
    {
        "x": 1,
        "y": 2
    }
]

def trees_encountered_part2():
    trees_encountered = 1
    map_ = open_file()

    for slope in slopes:
        nb_trees = 0
        x_position = 0
        for i in range(0,len(map_),slope["y"]):
            if map_[i][x_position] == "#":
                nb_trees += 1
            x_position = (x_position + slope["x"]) % len(map_[i])
        trees_encountered *= nb_trees

    return trees_encountered

# TESTS
# PART 1
print(trees_encountered_part1())
# output: 148

# PART 2
print(trees_encountered_part2())
# output: 727923200
