def get_and_validate_input(msg: str):

    valid: bool = False
    while (valid == False):
        user_input = input(msg)
        # isnumeric() will return true if string is numeric, and false if string is not numeric
        # cats and dogs user_input.isnumeric() returns false
        # 1000 user_input.isnumeric() returns true
        if (user_input.isnumeric()):
            # turns string into number
            number = int(user_input)
            if (number != 0):
                valid = True
                return number
        else:
            print('Please enter a numeric value')

def get_and_validate_goal(msg: str):

    while (True):
        user_input = input(msg)
        # isnumeric() will return true if string is numeric, and false if string is not numeric
        # cats and dogs user_input.isnumeric() returns false
        # 1000 user_input.isnumeric() returns true
        if (user_input[0] == '-'):
            user_input = user_input[1:]
        if (user_input.isnumeric()):
            # turns string into number
            return int(user_input)

        else:
            print('Please enter a numeric value')

# ("1000" == 1000) False

def main():
    
    # conditional -- something that will be true or false
    index = 0
    # index is a loop variable

    # while (index < 10):
    #     print(index)
    #     # index = index + 1
    #     # incrementing the index
    #     index += 1
    
    # for index in range(10):
    #     print(index)

    # deposit = get_and_validate_input('Please enter a deposit ')
    # interest_rate = get_and_validate_input('Please enter an interest rate ')
    # number_of_months = get_and_validate_input('Please enter an number of months')
    # goal = get_and_validate_goal('Please enter a goal ')

    # print(deposit, interest_rate, number_of_months, goal)

    string = "-1000"
    # - 0
    # 1 1
    # 0 2
    # 0 3
    # 0 4
    string_slice = string[1:]
    print(string_slice)
    # print(string.isnumeric())


    

if(__name__ == "__main__"):
    main()