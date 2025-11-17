def fib(num: int) -> int:
    """
    Recursively computes the n-th Fibonacci number.

    Args:
        num (int): The position in the Fibonacci sequence (non-negative integer).

    Returns:
        int: The Fibonacci number at position 'num'.
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

def main():
    """
    Prompts the user to enter a number and prints the corresponding Fibonacci number.
    Handles input errors and recursion errors gracefully.
    """
    try:
        num_input = input("Enter a number: ")
        num = int(num_input)

        if num <= 0:
            print("The number must be a natural number.")
            return

        print("Fibonacci number:", fib(num))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")

if __name__ == "__main__":
    main()
