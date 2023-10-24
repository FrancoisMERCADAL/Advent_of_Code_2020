FILE_NAME = 'bus_schedules.txt'

# PART 1
def parse_file_part1(file):
    depart_time = int(file.readline())
    buses_departs = [int(nb) for nb in file.readline().split(',') if nb != 'x']
    return depart_time, buses_departs

def get_coefficient_part1(file):
    depart_time, buses_departs = parse_file_part1(file)

    earliest_departures = []
    for bus in buses_departs:
        if depart_time % bus == 0:
            earliest_departures.append(int(depart_time/bus) * bus)
        else:
            earliest_departures.append((int(depart_time/bus) + 1) * bus)

    earliest_departure = min(earliest_departures)
    bus_id = buses_departs[earliest_departures.index(earliest_departure)]

    return (earliest_departure - depart_time) * bus_id

def shuttle_search_part1():
    file = open(FILE_NAME, "r")
    coefficient = get_coefficient_part1(file)
    file.close()
    return coefficient

# PART 2
def parse_file_part2(file):
    file.readline() # first line is useless
    buses_departs = file.readline().split(',')
    buses_departs = [int(element) if element.isnumeric() else element for element in buses_departs]
    return buses_departs

def get_coefficient_part2(file):
    buses_departs = parse_file_part2(file)
    time = 0
    bus_index = 1
    step_size = buses_departs[0]

    while True:
        if bus_index >= len(buses_departs):
            break
        
        if buses_departs[bus_index] == 'x':
            bus_index += 1
        else:
            time += step_size
            if (time + bus_index) % buses_departs[bus_index] == 0:
                step_size *= buses_departs[bus_index]
                bus_index += 1

    return time

def shuttle_search_part2():
    file = open(FILE_NAME, "r")
    coefficient = get_coefficient_part2(file)
    file.close()
    return coefficient

### TEST AREA
# Part 1
#print(shuttle_search_part1())
# Output: 2165

# Part 2
#print(shuttle_search_part2())
# Output: 534035653563227
