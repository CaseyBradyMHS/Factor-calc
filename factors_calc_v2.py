# functions go here

# puts a series of characters at start and end of text
def statement_generator(text, decoration):
    # make string with 5 characters
    ends = decoration * 5
    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions
def instructions():
    statement_generator("Instructions / information", "=")
    print('''
This program finds all factors of the number you enter. Simply enter a number
and the program will fnd the factors.

Complete as many calculations as necessary, pressing <enter>
at the end of each calculation or any key to quit. 
    ''')
    return ""


# number checker
def num_check(question, low, high):
    valid = False
    while not valid:

        error = f"please enter an integer that is more than or equal to {low} and less then {high}"

        try:
            # ask for a number
            response = int(input(question))

            # check number is more than / equal to lowest number allowed
            if response >= low:
                if response < high:
                    return response
                else:
                    print(error)
                    print()

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()


# gets factors, returns a sorted list.
def get_factors(var_to_factor):
    var_factor_list = []

    # find the square root (half way) and make it into an integer
    stop = int(var_to_factor ** 0.5)

    for item in range(1, stop + 1):
        remainder = var_to_factor % item

        if remainder == 0:
            var_factor_list.append(item)

            # calculate second factor and add it to the list
            factor_2 = var_to_factor // item
            var_factor_list.append((factor_2))

    var_factor_list.sort()
    return var_factor_list


# main routine


# heading
statement_generator("Factors Calculator", "-")

# display instructions
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factorised
    to_factor = num_check("Number?", 1, 200)

    if to_factor != 1:
        factor_list = get_factors(to_factor)
    else:
        factor_list = ""
        comment = "one is UNITY! It only has one factor. Itself."

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = f"{to_factor} is a prime number"
    elif len(factor_list) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    if to_factor == 1:
        heading = "One is special..."

    else:
        heading = f"Factors of {to_factor}"

    # output factors and comment
    factor_list_len = len(factor_list)
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(f"There are {factor_list_len} factors.")
    print(comment)

    print()
    keep_going = input("press <enter> to continue or any key to quit. ")
    print()

print()
print("Thanks you for using this factors calculator.")
print()
