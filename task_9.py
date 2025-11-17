def combin(num_1: int, num_2: int) -> int:
    """
    Recursively calculates the binomial coefficient (combinatorial number) C(n, k).

    Args:
        num_1 (int): The total number n (must be positive).
        num_2 (int): The number of chosen elements k (must be between 0 and n).

    Returns:
        int: The binomial coefficient C(n, k).
    """
    if num_2 == 0 or num_2 == num_1:
        return 1
    return combin(num_1 - 1, num_2 - 1) + combin(num_1 - 1, num_2)

def main():
    """
    Prompts the user to input two numbers and outputs their binomial coefficient.
    Handles invalid input and recursion errors gracefully.
    """
    try:
        num_1_input = input("Enter the first number: ")
        num_2_input = input("Enter the second number: ")

        num_1 = int(num_1_input)
        num_2 = int(num_2_input)

        if num_1 <= 0 or num_2 < 0:
            print("The numbers must be natural (positive) and the second should not exceed the first.")
            return
        if num_2 > num_1:
            print("The second number should not be greater than the first.")
            return

        print("Binomial coefficient:", combin(num_1, num_2))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")

if __name__ == "__main__":
    main()
