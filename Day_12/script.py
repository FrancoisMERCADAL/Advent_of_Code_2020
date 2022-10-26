file_name = 'instructions.txt'

cardinal_points = ['N','W','S','E']

# this variable can be used to determine for each key the left direction and the right direction
# the dictionary is built as follows:
# <key> : [<left_direction>,<right_direction>]
compass = {
    'N': ['W','E'],
    'W': ['S','N'],
    'S': ['E', 'W'],
    'E': ['N', 'S']
}

# PART 1
def turn_left(compass, faced_direction, angle_value):
    """
    determines the new faced direction of the ship when making a turn to the left
    
    Parameters:
    compass (dictionary)
    faced_direction (str)
    angle_value (int)
    
    Output:
    faced_position (str)
    """
    number_of_turns = int(angle_value/90)
    for i in range(number_of_turns):
        faced_direction = compass[faced_direction][0]
    return faced_direction

def turn_right(compass, faced_direction, angle_value):
    """
    determines the new faced direction of the ship when making a turn to the right
    
    Parameters:
    compass (dictionary)
    faced_direction (str)
    angle_value (int)
    
    Output:
    faced_position (str)
    """
    number_of_turns = int(angle_value/90)
    for i in range(number_of_turns):
        faced_direction = compass[faced_direction][1]
    return faced_direction

def calculate_manhattan_distance(position):
    """
    determines the Manhattan distance for a given position
    
    Parameters:
    position (dictionary)
    
    Output:
    (int): represents the Manhattan distance
    """
    return abs(position['N'] - position['S']) + abs(position['E'] - position['W'])

def ship_movements(file, cardinal_points, compass):
    """
    Reads every instruction contained in the file and implements every move
    
    Parameters:
    file (file type): file that contains all the instructions
    cardinal_points (str list): list that contains the cardinal points
    compass (str dictionary): dictionary used to determine for each key the left direction and the right direction
    
    Output:
    (int): the Manhattan distance
    """
    position = {
        'N': 0,
        'W': 0,
        'S': 0,
        'E': 0
    }
    
    faced_direction = 'E'
    
    for line in file:
        instruction = line[0]
        value = int(line[1:])
        
        if instruction in cardinal_points:
            position[instruction] += value
        elif instruction == 'F':
            position[faced_direction] += value
        else:
            if instruction == 'L':
                faced_direction = turn_left(compass, faced_direction, value)
            if instruction == 'R':
                faced_direction = turn_right(compass, faced_direction, value)
    
    return calculate_manhattan_distance(position)

def rain_risk_part1(file_name, cardinal_points, compass):
    file = open(file_name, "r")
    return ship_movements(file, cardinal_points, compass)

# PART 2
def move_ship_towards_waypoint(position, waypoint, value):
    """
    Apply changes to the ship's position following waypoint's values

    Parameters:
    position (str dictionary): variable that refers to the ship's position
    waypoint (str dictionary): dictionary that represents the waypoint the ship is heading to
    value (int)

    Output:
    position (str dictionary)
    """
    position['N'] += waypoint['N'] * value
    position['W'] += waypoint['W'] * value
    position['S'] += waypoint['S'] * value
    position['E'] += waypoint['E'] * value
    return position

def modify_waypoint(waypoint, cardinal_point, value):
    """
    Apply changes to the waypoint

    Parameters:
    waypoint (str dictionary): dictionary that represents the waypoint
    cardinal_point (str)
    value (int)

    Output:
    waypoint (str dictionary) with changes implemented in it
    """
    waypoint[cardinal_point] += value
    return waypoint

def rotate_waypoint_left(waypoint, angle_value):
    """
    determines the new waypoint after a turn to the left

    Parameters:
    waypoint (str dictionary): dictionary that represents the waypoint
    angle_value (int): value that represents the turn angle

    Outputs: 
    waypoint (str dictionary): dictionary that represents the new waypoint after the rotation to the left
    """
    number_turns = int(angle_value / 90)
    for i in range(number_turns):
        change_dictionary = {
            'N' : waypoint['N'],
            'W' : waypoint['W'],
            'S' : waypoint['S'],
            'E' : waypoint['E']
        }
        waypoint['N'] = change_dictionary['E']
        waypoint['W'] = change_dictionary['N']
        waypoint['S'] = change_dictionary['W']
        waypoint['E'] = change_dictionary['S']
    return waypoint

def rotate_waypoint_right(waypoint, angle_value):
    """
    determines the new waypoint after a turn to the right

    Parameters:
    waypoint (str dictionary): dictionary that represents the waypoint
    angle_value (int): value that represents the turn angle

    Outputs: 
    waypoint (str dictionary): dictionary that represents the new waypoint after the rotation to the right
    """
    number_turns = int(angle_value / 90)
    for i in range(number_turns):
        change_dictionary = {
            'N' : waypoint['N'],
            'W' : waypoint['W'],
            'S' : waypoint['S'],
            'E' : waypoint['E']
        }
        waypoint['N'] = change_dictionary['W']
        waypoint['W'] = change_dictionary['S']
        waypoint['S'] = change_dictionary['E']
        waypoint['E'] = change_dictionary['N']
    return waypoint

def ship_movements_with_waypoint(file, cardinal_points):
    """
    Reads every instruction contained in the file and implements every move with the new rules
    
    Parameters:
    file (file type): file that contains all the instructions
    cardinal_points (str list): list that contains the cardinal points
    
    Output:
    (int): the Manhattan distance
    """
    position = {
            'N': 0,
            'W': 0,
            'S': 0,
            'E': 0
        }
    waypoint = {
            'N': 1,
            'W': 0,
            'S': 0,
            'E': 10
        }
    
    for line in file:
        instruction = line[0]
        value = int(line[1:])
        
        if instruction == 'F':
            position = move_ship_towards_waypoint(position, waypoint, value)
        elif instruction in cardinal_points:
            waypoint = modify_waypoint(waypoint, instruction, value)
        else:
            if instruction == 'L':
                waypoint = rotate_waypoint_left(waypoint, value)
            if instruction == 'R':
                waypoint = rotate_waypoint_right(waypoint, value)
    return calculate_manhattan_distance(position)

def rain_risk_part2(file_name, cardinal_points):
    file = open(file_name, "r")
    return ship_movements_with_waypoint(file, cardinal_points)

# TESTS
print(rain_risk_part1(file_name, cardinal_points, compass))
# Output: 1631

print(rain_risk_part2(file_name, cardinal_points))
# Output: 58606