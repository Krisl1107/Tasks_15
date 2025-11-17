def maxlist(num_list):
    """
    Recursively finds the maximum element in a list of numbers.

    Args:
        num_list (list of int): The list of integers to search.

    Returns:
        int or None: The maximum element in the list, or None if the list is empty.
    """
    if len(num_list) == 0:
        return None
    if len(num_list) == 1:
        return num_list[0]
    return num_list[0] if num_list[0] > maxlist(num_list[1:]) else maxlist(num_list[1:])

def main():
    """
    Prompts the user to input a list of numbers separated by spaces,
    then finds and displays the maximum number using recursion.
    Handles invalid input and recursion errors gracefully.
    """
    try:
        num_input = input("Enter numbers separated by spaces: ")

        num_input_list = num_input.split()
        num_list = [int(num) for num in num_input_list]

        print("Maximum element:", maxlist(num_list))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")

if __name__ == "__main__":
    main()
