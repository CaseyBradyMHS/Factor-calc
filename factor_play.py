var_to_factor = 12

for item in range(1, var_to_factor + 1):
    remainder = var_to_factor % item

    print(f"Remainder = {var_to_factor} modulo {item} which is {remainder}")
    if remainder == 0:
        print(f"*** {item} is a factor of {var_to_factor} ***")

    print()
