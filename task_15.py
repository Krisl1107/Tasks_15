def ten_to_bin_1(num: int) -> str:
    """
    Recursively converts a decimal number to its binary representation as a string.

    Args:
        num (int): A non-negative integer to convert.

    Returns:
        str: A string representing the binary form of 'num'.
    """
    if num == 0:
        return ''
    return ten_to_bin_1(num // 2) + str(num % 2)

def ten_to_bin_2(num: int) -> str:
    """
    Converts a decimal number to its binary representation as a string.

    Args:
        num (int): A non-negative integer to convert.

    Returns:
        str: The binary representation of 'num' as a string.
    """
    if num == 0:
        return '0'
    return ten_to_bin_1(num)

def main():
    """
    Prompts the user for a number, validates input, and displays its binary form.
    Handles invalid input and recursion errors gracefully.
    """
    try:
        num_input = input("Enter a number: ")

        num = int(num_input)

        if num <= 0:
            print("The number must be a natural number.")
            return

        print("Binary form of the number:", ten_to_bin_2(num))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")

if __name__ == "__main__":
    main()
