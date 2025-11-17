def numbers(num: int) -> None:
    """
    Recursively prints each digit of the number in reverse order.

    Args:
        num (int): A positive integer to process.

    Returns:
        None: This function prints digits directly and does not return a value.
    """
    if num < 10:
        print(num)
    else:
        print(num % 10)
        numbers(num // 10)

def main():
    """
    Prompts the user to input an integer, validates it, and then prints its digits
    in reverse order using the recursive function `numbers`. Handles input errors
    and recursion errors gracefully.
    """
    try:
        num_input = input("Enter a number: ")

        num = int(num_input)

        if num <= 0:
            print("The number must be a natural number.")
            return

        print("Digits in reverse order:")
        numbers(num)

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")

if __name__ == "__main__":
    main()
