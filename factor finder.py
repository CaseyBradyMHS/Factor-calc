# modulo example

keep_going = ""
while keep_going == "":

    num_lollies = int(input("How many lollies?"))
    num_students = int(input("how many students?"))

    # Lollies per student divide
    lollies_per_student = num_lollies // num_students
    lollies_left = num_lollies % num_students

    # output fixer
    if lollies_left == 1:
        lolly_p1 = "lolly"
    else:
        lolly_p1 = "lollies"

    # output...
    print()
    print(f"You have {num_lollies} lollies and {num_students} students")
    print(f"Each student gets {lollies_per_student} lollies. ")
    print(f"You have {lollies_left} {lolly_p1} left")
    print()

    keep_going = input("Press <enter> to continue or any key to quit")
    print()

