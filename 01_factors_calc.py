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
This program assumes that images are being represented    
in 24 bit colour (ie: 24 bits per pixel). for text, we assume   
that ascii encoding is being used (8 bits per character).

Complete as many calculations as necessary, pressing <enter>
at the end of each calculation or any key to quit. 
    ''')
    return ""


# number checker
def num_check(question, low):

    valid = False
    while not valid:

        error = "please enter an integer that is more than or equal to {}".format(low)

        try:
            # ask for a number
            response = int(input(question))

            # check number is more than / equal to lowest number allowed
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()


# gets factors, returns a sorted list.
def get_factors(factor_variable):

    factor_list = []

    for item in range(1, var_to_factor + 1):
        remainder = var_to_factor % item

        if remainder == 0:
            factor_list.append(item)

    factor_list.sort()
    return factor_list

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
    var_to_factor = num_check("Number?", 1)

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "one is UNITY! It only has one factor. Itself."

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = f"{var_to_factor} is a prime number"
    elif len(factor_list) % 2 == 1:
        comment = f"{var_to_factor} is a perfect square"

    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = f"Factors of {var_to_factor}"

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

