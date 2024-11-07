def get_and_validate_input(msg: str, zero: bool):

    valid: bool = False
    while (valid is False):
        user_input = input(msg)
        # isnumeric() will return true if string is numeric, and false if string is not numeric
        # cats and dogs user_input.isnumeric() returns false
        # 1000 user_input.isnumeric() returns true

        filtered_str = ""

        for letter in user_input:
            if(letter != '.'):
                filtered_str += letter

        if (filtered_str.isnumeric()):
            # turns string into number
            number = float(user_input)

            if (zero == False):
                if (number != 0):
                    valid = True
                    return number
            else:
                valid = True
                return number

        print('Please enter a positive nonzero numeric value')

# ("1000" == 1000) False

def get_monthly_interest(deposit: float, monthly_interest_rate: float, months: float):
    for i in range(int(months)):
        # total amount in the account
        deposit = deposit + (deposit * monthly_interest_rate)
        print(deposit)

    return deposit


    # goal = 1000
    # depoit = 10
    # months_count = 0

    # while (deposit < goal):
        # continue compounding
        # increase months count by 1

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
    

    deposit = get_and_validate_input('Please enter a deposit ', False)
    interest_rate = get_and_validate_input('Please enter an interest rate ', False)
    number_of_months = get_and_validate_input('Please enter an number of months', False)
    goal = get_and_validate_input('enter your goal ', True)

    monthly_interest_rate = interest_rate / 12

    # print(f"The deposit you entered was: {deposit}, the interest rate is {interest_rate}, Number of months {number_of_months}, You goal is {goal}")
    # print("Monthly interest rate is:", monthly_interest_rate)

    print(get_monthly_interest(deposit, monthly_interest_rate, number_of_months))

    # print(deposit, interest_rate, number_of_months, goal)

    # string = "1000"

    # if ('-' in string):
    #     print('The user entered a negative number')
    # else:
    #     print('the user entered a positive number')


    
if(__name__ == "__main__"):
    main()