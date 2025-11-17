def mod_number(num_1: int, num_2: int) -> int:
    """
    Recursively computes the remainder of dividing num_1 by num_2.

    Args:
        num_1 (int): The dividend, a positive integer.
        num_2 (int): The divisor, a positive integer.

    Returns:
        int: The remainder after dividing num_1 by num_2.
    """
    if num_1 < num_2:
        return num_1
    else:
        return mod_number(num_1 - num_2, num_2)


def main():
    """
    Prompts the user to enter two natural numbers and prints the remainder
    of their division. Handles input errors and recursion errors gracefully.
    """
    try:
        num_1_input = input("Enter a natural number (dividend): ")
        num_2_input = input("Enter a natural number (divisor): ")

        num_1 = int(num_1_input)
        num_2 = int(num_2_input)

        if num_1 <= 0 or num_2 <= 0:
            print("The number must be a natural number.")
            return

        print("Remainder:", mod_number(num_1, num_2))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")


if __name__ == "__main__":
    main()
