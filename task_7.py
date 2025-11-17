def nod(num_1: int, num_2: int) -> int:
    """
    Computes the Greatest Common Divisor (GCD) of two positive integers using Euclid's algorithm.

    Args:
        num_1 (int): First positive integer.
        num_2 (int): Second positive integer.

    Returns:
        int: The GCD of num_1 and num_2.
    """
    if num_2 == 0:
        return num_1
    return nod(num_2, num_1 % num_2)

def main():
    """
    Prompts the user to input two natural numbers and prints their GCD.
    Handles input errors and recursion errors gracefully.
    """
    try:
        num_1_input = input("Enter the first number: ")
        num_2_input = input("Enter the second number: ")

        num_1 = int(num_1_input)
        num_2 = int(num_2_input)

        
        if num_1 <= 0 or num_2 <= 0:
            print("The numbers must be natural (positive integers).")
            return

        print("GCD:", nod(num_1, num_2))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")

if __name__ == "__main__":
    main()
