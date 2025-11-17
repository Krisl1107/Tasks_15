def pownum(num: float, degree: int) -> float:
    """
    Calculate num raised to the power of degree recursively.

    Args:
        num (float): The base number.
        degree (int): The exponent, must be a positive integer.

    Returns:
        float: The result of num raised to the power of degree.
    """
    if degree == 1:
        return num
    else:
        return num * pownum(num, degree - 1)


def main():
    """
    Prompts the user for input and calculates num^degree using the recursive function.
    Handles invalid inputs and recursion errors gracefully.
    """
    try:
        num_input = input("Enter number a: ")
        degree_input = input("Enter natural number n: ")

        num = float(num_input)
        degree = int(degree_input)

        if degree <= 0:
            print("Exponent must be a natural number (positive integer).")
            return

        result = pownum(num, degree)
        print("Result:", result)

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")


if __name__ == "__main__":
    main()
