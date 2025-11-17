def progress(num_1: float, dif: float, num_max: int) -> float:
    """
    Recursively computes the sum of the first 'num_max' terms of an arithmetic progression.

    Args:
        num_1 (float): The first term of the progression.
        dif (float): The common difference between terms.
        num_max (int): The number of terms to sum, must be a positive integer.

    Returns:
        float: The sum of the first 'num_max' terms.
    """
    if num_max == 1:
        return num_1
    else:
        return progress(num_1, dif, num_max - 1) + dif


def main():
    """
    Prompts the user to input the first term, number of terms, and common difference.
    Calculates the sum of the progression using a recursive function.
    Handles invalid inputs and recursion errors.
    """
    try:
        num_1_input = input("Enter the first term of the progression: ")
        num_max_input = input("Enter a natural number n: ")
        dif_input = input("Enter the common difference of the progression: ")

        num_1 = float(num_1_input)
        num_max = int(num_max_input)
        dif = float(dif_input)  

        if num_max <= 0:
            print("n must be a natural number (positive integer).")
            return

        print("Result:", progress(num_1, dif, num_max))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")


if __name__ == "__main__":
    main()
