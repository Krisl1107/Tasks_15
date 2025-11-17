def count(num: int) -> int:
    """
    Count the number of digits in a positive integer recursively.

    Args:
        num (int): A positive integer number.

    Returns:
        int: The count of digits in the number.
    """
    if num < 10:
        return 1
    else:
        return 1 + count(num // 10)


def main():
    """
    Prompts the user to enter a positive integer and displays the number of digits.
    Handles invalid input and recursion errors gracefully.
    """
    try:
        num_input = input("Enter a number: ")

        num = int(num_input)

        if num <= 0:
            print("The number must be a natural number (positive integer).")
            return

        print("Number of digits:", count(num))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")


if __name__ == "__main__":
    main()
