def ten_to_n(num: int, notation: int) -> str:
    """
    Recursively converts a positive integer 'num' from decimal to base 'notation'.

    Args:
        num (int): A positive integer to convert.
        notation (int): The target base (2 <= notation <= 16).

    Returns:
        str: The string representation of 'num' in the specified base.
    """
    digits = "0123456789ABCDEF"
    if num == 0:
        return ''
    return ten_to_n(num // notation, notation) + digits[num % notation]

def ten_to_n_1(num: int, notation: int) -> str:
    """
    Converts a positive integer 'num' from decimal to base 'notation', handling zero case.

    Args:
        num (int): A positive integer to convert.
        notation (int): The target base (2 <= notation <= 16).

    Returns:
        str: The string representation of 'num' in the specified base, or '0' if 'num' is zero.
    """
    if num == 0:
        return '0'
    return ten_to_n(num, notation)


def main():
    try:
        num_input = input("Enter number: ")
        notation_input = input("Enter notation: ")

        num = int(num_input)
        notation = int(notation_input)

        if num <= 0:
            print("It must be a natural number (positive integer).")
            return

        if notation < 2 or notation > 16:
            print("Incorrect number system")
            return

        result = ten_to_n_1(num, notation)
        print("Result:", result)

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")


if __name__ == "__main__":
    main()
