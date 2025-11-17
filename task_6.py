def degree5(num: int) -> int:
    """
    Recursively determines the exponent of 5 for a given number, if it is a power of 5.

    Args:
        num (int): A positive integer.

    Returns:
        int: The exponent such that 5 ** exponent = num, or -1 if num is not a power of 5.
    """
    if num == 1:
        return 0
    if num % 5 != 0:
        return -1
    result = degree5(num // 5)
    if result == -1:
        return -1
    else:
        return result + 1

def main():
    """
    Prompts the user to input a number and prints its power of 5 exponent.
    Handles input errors and recursion errors gracefully.
    """
    try:
        num_input = input("Enter a number: ")
        num = int(num_input)

        if num <= 0:
            print("The number must be a natural number.")
            return

        print("Power of 5:", degree5(num))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")


if __name__ == "__main__":
    main()
