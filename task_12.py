def search(num_list: list, num_find: int) -> int:
    """
    Recursively searches for a number in a list of integers.

    Args:
        num_list (list of int): The list of integers to search through.
        num_find (int): The number to find in the list.

    Returns:
        int:
            1 if the number is found in the list,
            0 if the list is empty or the number is not found.
    """
    if len(num_list) == 0:
        return 0
    if num_list[0] == num_find:
        return 1  
    return search(num_list[1:], num_find)

def main():
    """
    Prompts the user to input a list of numbers and a number to find.
    Uses recursion to determine if the number exists in the list.
    Handles invalid input and recursion errors gracefully.
    """
    try:
        num_input = input("Enter numbers separated by spaces: ")
        num_find_input = input("Enter the number to find: ")

        num_find = int(num_find_input)

        num_input_list = num_input.split()
        num_list = [int(num) for num in num_input_list]

        print("Result:", search(num_list, num_find))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")

if __name__ == "__main__":
    main()
