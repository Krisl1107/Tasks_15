def count(side_1: int, side_2: int) -> int:
    """
    Recursively counts the number of squares that can be cut from a rectangle
    with sides `side_1` and `side_2`, always cutting off the largest possible square
    at each step.

    Args:
        side_1 (int): Length of the first side of the rectangle (must be a positive integer).
        side_2 (int): Length of the second side of the rectangle (must be a positive integer).

    Returns:
        int: Total number of squares cut from the rectangle.
    """
    if side_1 == 0 or side_2 == 0:
        return 0
    if side_1 >= side_2:
        return side_1 // side_2 + count(side_1 % side_2, side_2)
    else:
        return side_2 // side_1 + count(side_1, side_2 % side_1)

def main():
    """
    Prompts the user to input the sides of a rectangle, validates input, and
    displays the total number of squares that can be cut from it.
    Handles invalid input and recursion errors gracefully.
    """
    try:
        side_1_input = input("Enter side_1: ")
        side_2_input = input("Enter side_2: ")

        side_1 = int(side_1_input)
        side_2 = int(side_2_input)

        if side_1 <= 0 or side_2 <= 0:
            print("It must be a natural number (positive integer).")
            return

        print("Result:", count(side_1, side_2))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")

if __name__ == "__main__":
    main()
