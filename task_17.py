def function1_0(num: int, divisor: int) -> bool:
    """
    Recursively checks whether 'num' is divisible by any number from 'divisor' up to sqrt(num).

    Args:
        num (int): The number to test for divisibility.
        divisor (int): The current divisor being tested.

    Returns:
        bool: True if 'num' is not divisible by any number from 'divisor' to sqrt(num), indicating 'num' is prime.
              False if 'num' is divisible by 'divisor', indicating 'num' is composite.
    """
    if divisor > num ** 0.5:
        return True
    if num % divisor == 0:
        return False
    return function1_0(num, divisor + 1)


def function1(num: int) -> int:
    """
    Determines if a given positive integer 'num' is a prime number.

    Args:
        num (int): The number to check for primality.

    Returns:
        int: 1 if 'num' is prime, 0 otherwise.
    """
    if num < 2:
        return 0
    if num == 2:
        return 1
    if function1_0(num, 2):
        return 1
    else:
        return 0
    
    
def main():
    try:
        num_input = input("Enter number: ")

        num = int(num_input)

        if num <= 0:
            print("It must be a natural number (positive integer).")
            return

        result = function1(num)
        print("Result:", result)

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")


if __name__ == "__main__":
    main()
