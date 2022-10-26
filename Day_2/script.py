file_name = 'passwords.txt'

# METHOD 1
def valid_passwords_count_method1(file):
    """
    determines the number of valid passwords in the file with the method n°1
    
    Parameters:
    file (file type): file that contains the passwords lines
    
    Output:
    count (int): count of valid passwords
    """
    count = 0
    for line in file:
        string = line.split(':')
        # head variable is designed as '<min_nb>-<max_nb> <character>'
        # the variable is directly splited with this type of output [<min_nb>-<max_nb>,<character>]
        head = string[0].split(' ')
        # password contains the password as a string variable (with whitespaces removed) 
        password = string[1].replace(' ','')
        
        min_max_numbers = head[0].split('-')
        character = head[1]
        min_number = int(min_max_numbers[0])
        max_number = int(min_max_numbers[1])
        
        character_count = password.count(character)
        
        if character_count >= min_number and character_count <= max_number:
            count += 1
    return count

def password_philosophy_part1(file_name):
    file = open(file_name, "r")
    return valid_passwords_count_method1(file)

# METHOD 2
def valid_passwords_count_method2(file):
    """
    determines the number of valid passwords in the file with the method n°2
    
    Parameters:
    file (file type): file that contains the passwords lines
    
    Output:
    count (int): count of valid passwords
    """
    count = 0
    for line in file:
        # the spliting method used here is the same as the one used with the method n°1
        string = line.split(':')
        head = string[0].split(' ')
        password = string[1].replace(' ','')
        
        min_max_indexes = head[0].split('-')
        character = head[1]
        min_index = int(min_max_indexes[0]) - 1 # since we are using indexes '-1' is necessary here
        max_index = int(min_max_indexes[1]) - 1
        
        if password[min_index] == character and password[max_index] != character:
            count += 1
        elif password[min_index] != character and password[max_index] == character:
            count += 1
        else:
            continue
    return count

def password_philosophy_part2(file_name):
    file = open(file_name, "r")
    return valid_passwords_count_method2(file)

# TESTS
print(password_philosophy_part1(file_name))
# output: 628

print(password_philosophy_part2(file_name))
# output: 705